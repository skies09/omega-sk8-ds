from django.conf.urls import url, include
from .views import home, about, deliveries, contact, faqs, setup, thanks

urlpatterns = [
url(r'^home/', home, name="home"),
url(r'^about/', about, name="about"),
url(r'^deliveries/', deliveries, name="deliveries"),
url(r'^contact/', contact, name="contact"),
url(r'^faqs/', faqs, name="faqs"),
url(r'^setup/', setup, name="setup"),
url(r'^thanks/', thanks, name="thanks"),
]