from typing import Union
from django.shortcuts import render
from django.http import HttpResponse, response
import datetime
from .models import Product, SearchHistory
# Create your views here.

def Home(request):
    if request.method == "GET":
        #Data Svaing for history of search
        SearchSTR = request.GET['Search']
        if SearchSTR == "":Data=SearchHistory(SearchContent= "Empty" )
        else:Data = SearchHistory(SearchContent = SearchSTR)
        Data.save()
        #Data Fetching for seacrh History
        SHistory = SearchHistory.objects.all().order_by('-SearchTime')
        #for logical part of search Engine
        SearchResults = Product.objects.filter(product_Name__icontains = SearchSTR)
        SearchResults1 = Product.objects.filter(product_desc__icontains = SearchSTR)
        FinalResult = SearchResults.union(SearchResults1)
        Context = {'SearchResults': FinalResult, 'Search':SearchSTR, 'SHistory': SHistory}
    return render(request, 'Shop/Home.html',Context)

def SearchHistry(request):
    return render(request,'Shop/Search.html')

def CreateData(request):
    if request.method == "GET":
        print("Inner___________True")
        Data = Product(product_Name=request.GET.get('Product_Name'), product_price=request.GET.get('Product_Price'), product_desc=request.GET.get('Product_Description'), product_Qty=request.GET.get('Product_Quntity'), product_creation_time=request.GET.get('Creation_Date'))
        Data.save()
    return render(request, 'Shop/Search.html')