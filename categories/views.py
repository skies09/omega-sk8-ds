from django.shortcuts import render
from products.models import Product

# Create your views here.

def product_filter(request, category):
    products = Product.objects.filter(category=category)
    return render(request, "products.html", {"products": products})