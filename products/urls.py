from . import views
from django.urls import path

app_name = "products.urls"
urlpatterns = [
    path('products/', views.products, name="products"),
    path('product/get/<int:id>/', views.single_product, name="single_product"),
    path('product/create/', views.create_product, name="create_product"),
    path('product/filter/', views.filter_products, name="filter_products"),
]
