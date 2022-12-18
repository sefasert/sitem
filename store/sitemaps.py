from django.contrib.sitemaps import Sitemap

from .models import Product

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    protocol = "https"

    def items(self):
        return Product.objects.filter(is_available=True)

    def location(self, obj: Product) -> str:
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.created_date
