from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, UserForm, UserProfileForm
from .models import Account, UserProfile

from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required


from django.conf import settings #settings'den al içe aktarmak için
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


from carts.views import _cart_id
from carts.models import Cart,CartItem

from orders.models import Order, OrderProduct

from django.views.decorators.csrf import requires_csrf_token
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    elif request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone_number = form.cleaned_data["phone_number"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            username = email.split("0")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()

            #USER ACTIVATION  #save yaptıktan sonra
            from_email = settings.DEFAULT_FROM_EMAIL
            current_site = get_current_site(request)
            mail_subject = "hesabını aktive et"
            message = render_to_string("accounts/emails/account_verification_email.html" , {
                "user": user,
                "domain": current_site,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, from_email, to=[to_email])
            send_email.send()
            return redirect("/accounts/login/?command=verification&email:"+email)
    else:
        form = RegistrationForm()

    context = {
        "form": form
    }
    return render(request, "accounts/register.html", context)


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "hesabınız aktive edildi giriş yapabilirsiniz")
        return redirect("login")
    else:
        messages.error(request, "geçersiz aktivasyon linki")
        return redirect("register")


@requires_csrf_token
def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    elif request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.error(request, "e-posta yada şifre yanlış")
            return redirect("login")
    return render(request, "accounts/login.html")


def logout(request):
    auth.logout(request)
    return redirect("home")


@login_required(login_url="login")
def dashboard(request):
    orders = Order.objects.order_by("created_at").filter(user_id=request.user.id, is_ordered=True)
    orders_count = orders.count()
    context = {
        "orders_count": orders_count
    }
    return render(request, "accounts/dashboard.html", context)

@login_required(login_url="login")
def my_orders(request):
    orders = Order.objects.filter(user=request.user, is_ordered=True).order_by("-created_at")
    context = {
        "orders": orders
    }
    return render(request, "accounts/my_orders.html", context)


def forgot_password(request):
    if request.method == "POST":
        email = request.POST["email"]

        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            #USER PASSWORD RESET
            from_email = settings.DEFAULT_FROM_EMAIL
            current_site = get_current_site(request)  #current site şuanlık localhost
            mail_subject = "Şifreni değiştir"
            message = render_to_string("accounts/emails/reset_password_email.html" , {
                "user": user,
                "domain": current_site,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, from_email, to=[to_email])
            send_email.send()

            messages.success(request, "şifre değiştirme isteğiniz epostanıza gönderildi")
            return redirect("/accounts/forgot_password/?command=reset_password_to:"+email)

        else:
            messages.error(request, "böyle email mevcut değil")
            return redirect("forgot_password")
    return render(request, "accounts/forgot_password.html")


def reset_password_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session["uid"] = uid
        return redirect("reset_password")
    else:
        messages.error(request, "geçersiz link,yeniden link isteği gönderin")
        return redirect("forgot_password")

    return render(request, "accounts/reset_password_validate.html")



def reset_password(request):
    if request.method == "POST":
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            pk = request.session.get("uid")
            user = Account.objects.get(pk=pk)
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request, "şifre değiştirme başarılı giriş yapabilirsiniz")
            return redirect("login")

        else:
            messages.error(request, "şifre eşleşmiyor")
            return redirect("reset_password")

    else:
        return render(request, "accounts/reset_password.html")



@login_required(login_url="login")
def edit_profile(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user) #instance güncellenecek bilgilerin gözükmesi için
        profile_form = UserProfileForm(request.POST, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profilin guncellendi")
            return redirect("edit_profile")
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=userprofile)
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, "accounts/edit_profile.html", context)


@login_required(login_url="login")
def change_password(request):
    if request.method == "POST":
        current_password = request.POST["current_password"]
        new_password = request.POST["new_password"]
        confirm_password = request.POST["confirm_password"]

        user = Account.objects.get(username__exact=request.user.username)
#mevcut olan şifre doğruysa yeni şifre işlemini gerçekleştir
        if new_password == confirm_password: #yeni şifreleri yaz
            success = user.check_password(current_password) #eski şifre doğruysa kontrol et
            if success:
                user.set_password(new_password) # eski şifre doğruysa yeni şifre yaz
                user.save()
                messages.success(request, "Şifre başarılı bir şekilde güncellendi") #işlem başarılıysa ekrana yazdır
                return redirect("change_password")
            else:
                messages.error(request, "Şimdiki şifreyi girin") # değilse tekrar dene eski şifreyi
                return redirect("change_password")
        else:
            messages.error(request, "Şifreler eşleşmiyor!")  # değilse yeni şifreler eşleşmiyor
            return redirect("change_password")

    return render (request, "accounts/change_password.html")


@login_required(login_url="login")
def order_detail(request, order_id): # order_id ile url de gözükür sipariş no'su
    order_detail = OrderProduct.objects.filter(order__order_number=order_id) #__ foreignkey olduğu için
    order = Order.objects.get(order_number=order_id) #sipariş no

    context = {
        "order_detail": order_detail,
        "order": order,
    }
    return render(request, "accounts/order_detail.html", context)
