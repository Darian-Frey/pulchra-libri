from django.urls import path
from .views import all_products, product_detail, add_product, edit_product, delete_product, like_product


urlpatterns = [
    path('', all_products, name='products'),
    path('<int:product_id>/', product_detail, name='product_detail'),
    path('add/', add_product, name='add_product'),
    path('edit/<int:product_id>/', edit_product, name='edit_product'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
    path('like/', like_product, name='like_product'),
]
