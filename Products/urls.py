# ecommerce_project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet
from Orders.views import OrderViewSet
from User.views import register_user

namespace="Products"

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
    path('products/<int:pk>/upload_images/', ProductViewSet.as_view({'post': 'upload_images'}),
         name='product-upload-images'),

]