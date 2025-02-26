import requests
from requests.exceptions import RequestException
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from products.models import Product
from products.forms import ProductForm



def homePage(request):
    return render(request, 'index.html')

def products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            context = {
                'products': Product.objects.all(),
                'form': form
            }
            return render(request, 'products.html', context)


    products = Product.objects.all()
    context = {'products': products, 'form': ProductForm()}
    return render(request, 'products.html', context)

@login_required
def profile(request):
    return render(request, 'profile.html')

def login(request):
    return render(request, 'login.html')

def post(request):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        response.raise_for_status()
        return JsonResponse(response.json())
    except RequestException as e:
        return HttpResponse("Service unavailable", status=503)