from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='designproducts'),
    path('<int:designproduct_id>/', views.product_detail, name='product_detail'),  # noqa
    # Likes
    path('<int:designproduct_id>/like_toggle/', views.like_toggle, name='like_toggle'),  # noqa
    path('add/', views.add_designproduct, name='add_designproduct'),
    path('edit/<int:designproduct_id>/', views.edit_designproduct, name='edit_designproduct'),  # noqa
    path('delete/<int:designproduct_id>/', views.delete_designproduct, name='delete_designproduct'),  # noqa
    # User comments
    path('add_comment/<int:designproduct_id>/', views.add_comment, name='add_comment'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    # User favorite
    path('product-favorite/', views.product_favorite, name='product_favorite'),
    path('add_favorite/<int:designproduct_id>/', views.add_favorite, name='add_favorite'),
    path('remove_favorite/<int:designproduct_id>/', views.remove_favorite, name='remove_favorite'),
]

