from django.shortcuts import render

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