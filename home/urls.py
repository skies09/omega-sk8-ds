from django.conf.urls import url, include
from .views import home
from .views import deliveries
from .views import contact


urlpatterns = [
url(r'^home/', home, name="home"),
url(r'^deliveries/', deliveries, name="deliveries"),
url(r'^contact/', contact, name="contact"),
]