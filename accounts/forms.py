from django import forms
from .models import Account, UserProfile

from django.contrib.auth import password_validation

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}), help_text=password_validation.password_validators_help_text_html)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "tekrar şifre girin", "class": "form-control" }))
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "(email onayı için)", "class": "form-control" }))

    class Meta:
        model = Account
        fields = ["first_name", "email", "password"]

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        email = cleaned_data.get("email")

        if password != confirm_password:
            raise forms.ValidationError("şifre eşleşmiyor")
        password_validation.validate_password(self.cleaned_data.get('password',None))
        return self.cleaned_data


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields["first_name"]
        self.fields["email"]
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"

class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ("first_name",)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("address_line", "city", "state", "phone_number")

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
