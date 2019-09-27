from django.conf.urls import url, include
from .views import all_products, product_filter, product_detail


urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'(?P<category>\w+)/$', product_filter, name='product-filter'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail'),
]