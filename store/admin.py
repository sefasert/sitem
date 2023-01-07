from django.contrib import admin

from .models import Product, ProductGallery

import admin_thumbnails

from django.utils.html import format_html
# Register your models here.

@admin_thumbnails.thumbnail("image")
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("product_name",)}
    list_display        = ("product_name", "brand", "thumbnail", "price", "stock", "yeni", "category", "durum", "modified_date", "is_available")
    search_fields       = ("product_name", "brand")
    list_per_page       = 20
    inlines             = [ProductGalleryInline]
    list_editable = ['stock', "yeni", "brand"]

    def thumbnail(self, object):
        return format_html('<img src="{}" width="80"/>'.format(object.images.url))
    thumbnail.short_description = "Image"


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductGallery)
