from django.db import models

from accounts.models import Account
from store.models import Product

from accounts.utils import send_notif
# Create your models here.

class Order(models.Model):
    STATUS = (
    ("Yeni", "yeni"),
    ("Beklemede", "beklemede"),
    ("Onay", "onay"),
    ("İptal", "iptal"),
    )

    user            = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    order_number    = models.CharField(max_length=20)
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    phone           = models.CharField(max_length=15)
    email           = models.CharField(max_length=50)
    address_line    = models.CharField(max_length=150)
    state           = models.CharField(max_length=50)
    city            = models.CharField(max_length=50)
    order_total     = models.FloatField()
    status          = models.CharField(max_length=10, choices=STATUS, default="yeni")
    ip              = models.CharField(max_length=20, blank=True)
    is_ordered      = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        if self.pk is not None:
            #update
            orig = Order.objects.get(pk=self.pk)
            if orig.is_ordered != self.is_ordered:
                mail_template = "accounts/emails/admin_approval_email.html"
                context = {
                    "user": self.user,
                    "is_ordered": self.is_ordered,
                }
                if self.is_ordered == True:
                    #send email
                    mail_subject = "Siparişiniz Onaylandı"
                    send_notif(mail_subject, mail_template, context)
                else:
                    #send email
                    mail_subject = "Siparişiniz Onaylanmadı"
                    send_notif(mail_subject, mail_template, context)
                    
        return super(Order, self).save(*args, **kwargs)


class OrderProduct(models.Model):
    order           = models.ForeignKey(Order, on_delete=models.CASCADE)
    user            = models.ForeignKey(Account, on_delete=models.CASCADE)
    product         = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity        = models.IntegerField()
    product_price   = models.FloatField()
    ordered         = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name
