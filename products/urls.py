from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/edit', views.editProduct, name='edit-product'),
    path('newproduct', views.newProduct, name='new-product'),
    path('list', views.productList, name='product-list'),
    path('list/analytics', views.productListAnalytics, name='product_list_analytics'),
    path('<int:id>/pricing', views.productPricing2, name='product-pricing'),

]