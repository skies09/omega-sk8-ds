from django.conf.urls import url, include
from .views import all_products
from .views import product_filter

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'(?P<category>\w+)/$', product_filter, name='product-filter'),
]