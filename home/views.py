from django.shortcuts import render

# Create your views here.
def home(request):
    """A view that displays the home page"""
    return render(request, "home.html")

def deliveries(request):
    """A view that displays the contact page"""
    return render(request, "deliveries.html")

def contact(request):
    """A view that displays the contact page"""
    return render(request, "contact.html")