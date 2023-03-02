from PIL import Image

from django.db import models

from category.models import Category

from django.urls import reverse

from ckeditor.fields import RichTextField

# Create your models here.

class Product(models.Model):

    BRAND_CHOICE = {
        ("-", ""),
        ("Vestel-Toshiba-Profilo", "vestel-toshiba-profilo"),
        ("Vestel-SEG", "vestel-seg"),
        ("Vestel-Regal", "vestel-regal"),
        ("Vestel-Techwood-Regal", "vestel-techwood-regal"),
        ("Vestel", "vestel"),
        ("Vestel-ALBA", "vestel-alba"),
        ("Vestel, Hi-Level", "vestel,hi-level"),
        ("PHILIPS", "philips"),
        ("Dreamstar", "dreamstar"),
        ("SAMSUNG", "samsung"),
        ("SANYO", "sanyo"),
        ("SUNNY", "sunny"),
        ("AWOX", "awox"),
        ("Dijitsu", "dijitsu"),
        ("LG", "lg"),
        ("Profilo", "profilo"),
        ("NEXT", "next"),
        ("Arçelik-Beko-Grundig-Altus", "arcelik-beko-grundig-altus"),
        ("Arçelik-Beko-Grundig", "arçelik-beko-grundig"),
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
        ("Panasonic", "panasonic"),
        ("Nordmende", "nordmende"),
        ("Lifemaxx", "lifemaxx"),
        ("Osawa", "osawa"),
        ("Hisense", "hisense"),
        ("SEG", "seg"),
        ("Hi-Level", "hi-level"),
        ("RONAX-TELENOVA", "ronax-telenova"),
        ("BOE", "boe"),
        ("WOON", "woon"),
        ("SHARP", "sharp"),
        ("REGAL", "regal"),
        ("AUO", "auo"),
        ("Acer", "acer"),
        ("DARFON", "darfon"),
        ("INNOLUX", "innolux"),
        ("CHIMEI", "chimei"),
        ("VESTEL-SEG-REGAL", "vestel-seg-regal"),
        ("MEGMEET", "megmeet"),
    }

    DURUM_CHOICE = {
        ("Sıfır", "0"),
        ("2.EL", "2"),
    }

    YENI_CHOICE = {
        ("Yeni", "yeni"),
    }

    EKRAN_CHOICE = {
        ("LED", "led"),
        ("LCD", "lcd"),
        ("Plazma", "plazma"),
        ("LED-LCD", "led-lcd")
    }

    category      = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)
    product_name  = models.CharField(max_length=200, blank=False)
    slug          = models.SlugField(max_length=200, unique=True, blank=False)
    brand         = models.CharField(max_length=100, choices=BRAND_CHOICE, blank=True)
    durum         = models.CharField(max_length=50, choices=DURUM_CHOICE, blank=True)
    yeni          = models.CharField(max_length=10, choices=YENI_CHOICE, blank=True)
    price         = models.IntegerField()
    images        = models.ImageField(upload_to= "photos/products", blank=True, null=True)
    webp          = models.ImageField(upload_to= "webp/products", blank=True, null=True)
    images2       = models.ImageField(upload_to= "photos2/products", blank=True, null=True)
    webp2         = models.ImageField(upload_to= "webp2/products", blank=True, null=True)
    stock         = models.IntegerField()
    ekran         = models.CharField(max_length=10, choices=EKRAN_CHOICE, blank=True)
    tags          = models.TextField(max_length=1000, blank=True)
    description   = RichTextField(blank=True)
    is_available  = models.BooleanField(default=False)
    created_date  = models.DateField(auto_now_add=True)
    sontarih      = models.DateTimeField(default=False, blank=True)
    modified_date = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0, blank=True)

    def get_absolute_url(self): #kategori slug ve ürünün kendi slug'ı al
        return reverse("product_detail", args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.images:
            img = Image.open(self.images.path)
            if img.height > 1600 or img.width > 1600:
                output_size = (1600, 1600)
                img.thumbnail(output_size)
                img.save(self.images.path)

        if self.images2:
            img = Image.open(self.images2.path)
            if img.height > 1600 or img.width > 1600:
                output_size = (1600, 1600)
                img.thumbnail(output_size)
                img.save(self.images2.path)


class Related_Product(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    benzerresimlink = models.CharField(max_length=200, blank=True)
    benzerad  = models.CharField(max_length=200)
    benzerlink = models.CharField(max_length=200)
    benzerfiyat = models.IntegerField()

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name_plural = "related product"
