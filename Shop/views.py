from typing import Union
from django.shortcuts import render
from django.http import HttpResponse, response
import datetime
from .models import Product, SearchHistory
# Create your views here.

def Home(request):
    if request.method == "GET":
        SearchSTR = request.GET['Search']

        #Data Svaing for history of search
        Data = SearchHistory(SearchContent = SearchSTR)
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