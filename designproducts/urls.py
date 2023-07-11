from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='designproducts'),
    path('<int:designproduct_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_designproduct, name='add_designproduct'),
    path('edit/<int:designproduct_id>/', views.edit_designproduct, name='edit_designproduct'),
    path('delete/<int:designproduct_id>/', views.delete_designproduct, name='delete_designproduct'),
    ]
