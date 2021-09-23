from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('wish_list/', views.wish_list, name='wish_list'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('remove_wish_list/<product_id>', views.remove_wish_list, name='remove_wish_list'),
]
