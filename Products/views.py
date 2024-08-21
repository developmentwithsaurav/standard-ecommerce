from django.shortcuts import render

# Create your views here.
# store/views.py

from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['post'])
    def upload_images(self, request, pk=None):
        product = self.get_object()
        images = request.FILES.getlist('images')

        for image in images:
            ProductImage.objects.create(product=product, image=image)

        return Response({'status': 'Images uploaded'}, status=status.HTTP_200_OK)
