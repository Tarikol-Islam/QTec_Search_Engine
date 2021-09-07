from django.urls import path
from . import views
urlpatterns=[
        path('Home', views.Home, name='ShopHome'),
        path('',views.SearchHistry,name='SearchHistry'),
]