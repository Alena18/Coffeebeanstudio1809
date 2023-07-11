from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='designproducts'),
    path('<int:designproduct_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_designproduct, name='add_designproduct'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    ]
