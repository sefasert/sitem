from django.contrib import admin

from .models import Order, OrderProduct
# Register your models here.

class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ("user", "product", "product_price", "quantity")
    can_delete = False
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ["first_name", "order_number", "email", "phone", "state", "city", "order_total", "status", "is_ordered"]
    list_filter = ["status"]
    readonly_fields = ("order_number", "email", "user", "address_line", "state", "city", "phone", "first_name", "ip", "phone", "order_total")
    search_fields = ["order_number", "first_name", "phone", "email"]
    list_per_page = 20
    can_delete = False
    inlines = [OrderProductline]

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "product_price", "quantity", "ordered"]
    list_filter = ["user"]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
