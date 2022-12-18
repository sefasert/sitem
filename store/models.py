from django.db import models

from category.models import Category

from django.urls import reverse

from ckeditor.fields import RichTextField

from PIL import Image


# Create your models here.

class Product(models.Model):

    BRAND_CHOICE = {
        ("-", ""),
        ("Botech", "botech"),
        ("CVS", "cvs"),
        ("VESTEL", "vestel"),
        ("PHILIPS", "philips"),
        ("TCL", "tcl"),
        ("TECHNOBOX", "technobox"),
        ("Dreamstar", "dreamstar"),
        ("SAMSUNG", "samsung"),
        ("SANYO", "sanyo"),
        ("TELENOVA", "telenova"),
        ("SUNNY", "sunny"),
        ("AWOX", "awox"),
        ("Dijitsu", "dijitsu"),
        ("LG", "lg"),
        ("Profilo", "profilo"),
        ("NEXT", "next"),
        ("Arçelik-Beko-Grundig-Altus", "arcelik-beko-grundig-altus"),
        ("GEEPAS", "geepas"),
        ("ROWELL", "rowell"),
        ("ONVO", "onvo"),
        ("Next", "next"),
        ("Skytech", "skytech"),
        ("SONY", "sony"),
        ("YUMATU", "yumatu"),
        ("Homstar", "homstar"),
        ("Premier", "premier"),
        ("AXEN", "axen"),
        ("SUNNY-AXEN" , "sunny-axen"),
        ("Navitech", "navitech"),
        ("TOSHIBA", "toshiba"),
        ("Panasonic", "panasonic"),
        ("Nordmende", "nordmende"),
    }

    DURUM_CHOICE = {
        ("Sıfır", "0"),
        ("2.EL", "2"),
    }

    category      = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    product_name  = models.CharField(max_length=200)
    slug          = models.SlugField(max_length=200, unique=True)
    brand         = models.CharField(max_length=50, choices=BRAND_CHOICE, blank=True, null=True)
    durum         = models.CharField(max_length=50, choices=DURUM_CHOICE, blank=True, null=True)
    price         = models.IntegerField()
    images        = models.ImageField(upload_to= "photos/products")
    stock         = models.IntegerField()
    tags          = models.CharField(max_length=400, blank=True)
    description   = RichTextField(blank=True)
    is_available  = models.BooleanField(default=False)
    created_date  = models.DateField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.images.path)
        if img.height > 2000 or img.width > 2000:
            output_size = (2000, 2000)
            img.thumbnail(output_size)
            img.save(self.images.path)


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="store/products", max_length=255)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name_plural = "product gallery"
