from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def product_filter(request, category):
    products = Product.objects.filter(category=category)
    return render(request, "products.html", {"products": products})

def product_detail(request, pk):
    products = Product.object.get(products, pk=pk)
    return render(request, "productdetail.html", {'products': products})