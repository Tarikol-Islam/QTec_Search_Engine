from django.contrib.auth.models import User
from Shop.models import Product
from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ProductSerializer
# Create your views here.

class ProductApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductApiNewView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all().order_by('-product_ID')[:1]
    serializer_class = ProductSerializer

