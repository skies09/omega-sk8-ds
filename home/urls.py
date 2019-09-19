from django.conf.urls import url, include
from .views import home
from .views import deliveries
from .views import contact
from .views import faqs
from .views import setup
from .views import thanks


urlpatterns = [
url(r'^home/', home, name="home"),
url(r'^deliveries/', deliveries, name="deliveries"),
url(r'^contact/', contact, name="contact"),
url(r'^faqs/', faqs, name="faqs"),
url(r'^setup/', setup, name="setup"),
url(r'^thanks/', thanks, name="thanks"),
]