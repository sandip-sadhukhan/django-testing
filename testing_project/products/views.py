from django.shortcuts import render
from .models import Product

def homePage(request):
    return render(request, 'index.html')

def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)