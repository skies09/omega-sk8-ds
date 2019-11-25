from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from decimal import Decimal
from products.models import Product
from .models import Coupon
from .forms import CouponApplyForm
from .views import coupon_apply, Coupon


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})
    coupon_id = request.session.get('coupon_id', int())


    cart_items = []
    total = 0
    product_count = 0
    coupon_total = 0

    try:
        code = Coupon.objects.get(id=coupon_id)

    except Coupon.DoesNotExist:
        code = None

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        
        if code != None:
            discount = (code.discount/Decimal('100'))*total
            coupon_total = total - discount
        else:
            coupon_total = total
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
        
    coupon_form = CouponApplyForm(request.POST)
        
        
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count, 'code': code, 'coupon_id': coupon_id, 'coupon_total': coupon_total, 'CouponApplyForm': CouponApplyForm}
