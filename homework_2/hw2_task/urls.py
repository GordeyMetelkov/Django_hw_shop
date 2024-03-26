from django.urls import path
from . import views

urlpatterns = [
    path('orders_by_client/<int:client_id>', views.get_all_orders_by_client, name='orders_by_client'),
    path('orders_by_time/<int:client_id>/<int:time>', views.get_orders_by_time, name='orders_by_time'),
    path('product/<int:product_id>/', views.get_product, name='get_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name= 'edit_product'),
]
