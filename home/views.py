from django.shortcuts import render
from products.models import Product

# Create your views here.
def home(request):
    """A view that displays the home page"""
    return render(request, "home.html")

def deliveries(request):
    """A view that displays the deliveries page"""
    return render(request, "deliveries.html")

def contact(request):
    """A view that displays the contact page"""
    return render(request, "contact.html")

def faqs(request):
    """A view that displays the help page"""
    return render(request, "help.html")


def setup(request):
    """A view that displays the setup page"""
    return render(request, "setup.html")

def thanks(request):
    """A view that displays the thanks page"""
    return render(request, "thanks.html")

def product_filter(request, category):
    products = Product.objects.filter(category=category)
    return render(request, "products.html", {"products": products})