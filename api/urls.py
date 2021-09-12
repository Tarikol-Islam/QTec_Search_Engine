from .views import ProductApiView, ProductApiDetailView, ProductApiNewView
from django.urls import path

urlpatterns = [
    path('product/', ProductApiView.as_view()),
    path('product/<int:pk>', ProductApiDetailView.as_view()),
    path('product/new', ProductApiNewView.as_view())
]
