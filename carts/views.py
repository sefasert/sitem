from django.shortcuts import render, redirect, get_object_or_404

from store.models import Product
from category.models import Category
from .models import Cart, CartItem

from orders.forms import OrderForm
from orders.models import Order, OrderProduct

from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required

import datetime

from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id)  #ürünü al
    #if user authenticated
    if current_user.is_authenticated:
        try:
            cart_item = CartItem.objects.get(product=product, user=current_user)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                user = current_user
            )
            cart_item.save()
        return redirect ("cart")

    #if user is not authenticated
    else:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                cart_id = _cart_id(request)
            )
        cart.save()

        try:
            cart_item = CartItem.objects.get(product=product, cart=cart)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                cart = cart
            )
            cart_item.save()
        return redirect ("cart")


def remove_cart(request, product_id, cart_item_id):  #stok eksiltme ve 0 ise ürünü kartdan silme
    product   = get_object_or_404(Product, id=product_id)
    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
        else:
            cart      = Cart.objects.get(cart_id=_cart_id(request))
            cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect("cart")

def remove_cart_item(request, product_id, cart_item_id):  #ürünü kartdan silme
    product   = get_object_or_404(Product, id=product_id)
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
    else:
        cart      = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
    cart_item.delete()
    return redirect("cart")


def cart(request, total=0, quantity=0, cart_items=None):
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
    except ObjectDoesNotExist:
        pass #nesne yoksa yoksay

    context = {
        "total"      : total,
        "quantity"   : quantity,
        "cart_items" : cart_items,
    }
    return render(request, "store/cart.html", context)


@login_required(login_url= "login")
def checkout(request):
    current_user = request.user
    cart_items = CartItem.objects.filter(user_id=current_user.id)
    total = 0
    for cart_item in cart_items:
        total += cart_item.product.price * cart_item.quantity

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data["first_name"]
            data.phone = form.cleaned_data["phone"]
            data.user_id = current_user.id
            data.email = form.cleaned_data["email"]
            data.address_line = form.cleaned_data["address_line"]
            data.state = form.cleaned_data["state"]
            data.city = form.cleaned_data["city"]
            data.order_total = total
            data.ip = request.META.get("REMOTE_ADDR")
            data.save()
            #oluştur order numara
            yr = int(datetime.date.today().strftime("%Y"))
            dt = int(datetime.date.today().strftime("%d"))
            mt = int(datetime.date.today().strftime("%m"))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%Y%m%d")  #20221231
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            cart_items = CartItem.objects.filter(user_id=current_user.id)
            for cart_item in cart_items:
                detail = OrderProduct()
                detail.order_id  = data.id
                detail.product_id = cart_item.product_id
                detail.user_id = current_user.id
                detail.quantity = cart_item.quantity
                detail.product_price = cart_item.product.price
                detail.save()

                product = Product.objects.get(id=cart_item.product_id)
                product.stock -= cart_item.quantity
                product.save()

            CartItem.objects.filter(user_id=current_user.id).delete()
            request.session["cart_items"]=0

            order = Order.objects.get(user=request.user, order_number=order_number)
            mail_subject = "Siparişiniz Bize Ulaştı"
            message = render_to_string("orders/order_recieved_email.html" , {
                "user": request.user,
                "order": order,
            })
            to_email = request.user.email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            return render (request, "orders/order_completed.html", {"order": order})

    form = OrderForm()
    context = {
        "total"      : total,
        "cart_items" : cart_items,
    }
    return render(request, "store/checkout.html", context)
