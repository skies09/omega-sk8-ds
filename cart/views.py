from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from decimal import Decimal
from .models import Coupon
from .forms import CouponApplyForm
from django.utils import timezone


# Create your views here.
def view_cart(request):
    coupon_form = CouponApplyForm()
    """A View that renders the cart contents page"""
    return render(request, "cart.html", {'coupon_form':coupon_form})


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('home'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, id):
    """
    Remove the specified product from the cart
    """
    cart = request.session.get('cart', {})

    cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


@require_http_methods(["GET", "POST"])
def coupon_apply(request):
    now = timezone.now()
    coupon_form = CouponApplyForm(request.POST)
    if coupon_form.is_valid():
        code = coupon_form.cleaned_data['code']
    try:
        coupon = Coupon.objects.get(code=code, active=True)
        request.session['coupon_id'] = coupon.id
        messages.success(request, 'Coupon applied')
    except Coupon.DoesNotExist:
        request.session['coupon_id'] = None
        messages.warning(request, 'Coupon not accepted')
        return redirect ('view_cart')
    else:
        return redirect('view_cart')

