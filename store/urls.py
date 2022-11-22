from django.urls import path,include
from . import views
from .views import ProductView, ProductDetailView


app_name = 'store'

urlpatterns = [
    path('health_check',  views.home, name="home"),
    path("products/", ProductView.as_view(), name="products"),
    path("products/<int:pk>", ProductDetailView.as_view(), name="products"),
    path('cache/', views.view_cached_products, name="cache-products"),
]