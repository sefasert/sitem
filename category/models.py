from django.db import models

from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name =  models.CharField(max_length=50, unique=True)
    slug          =  models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def get_url(self):
        return reverse("products_by_category", args=[self.slug])

    def __str__(self):
        return self.category_name


class Setting(models.Model):
    title         = models.CharField(max_length=50, blank=True)
    keywords      = models.CharField(max_length=400, blank=True)
    description   = models.CharField(max_length=350, blank=True)
    telefon       = models.CharField(max_length=50, blank=True)
    adres         = models.CharField(max_length=50, blank=True)
    saat          = models.CharField(max_length=50, blank=True)
    copy          = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return self.title
