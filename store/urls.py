from django.urls import path
from . import views




urlpatterns = [
    path("", views.home, name="home"),
    path("index/", views.store, name="store"),
    path("category/<slug:category_slug>/", views.store, name="products_by_category"), #kategoriye göre ürünler
    path("category/<slug:category_slug>/<slug:product_slug>/", views.product_detail, name="product_detail"),
    path("search/", views.search, name="search"),
    path("otoyazi/", views.otoyazi, name="otoyazi"),
    path("filter_results/", views.filter_results, name="filter_results"),

]
