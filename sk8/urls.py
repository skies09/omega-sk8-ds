"""sk8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from home.views import home
from accounts import urls as urls_accounts
from home import urls as urls_home
from products import urls as urls_products
from categories import urls as urls_categories
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from search import urls as urls_search
from blog import urls as urls_blog


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^home/', include(urls_home)),
    url(r'^products/', include(urls_products)),
    url(r'^categories/', include(urls_categories)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
    url(r'^blog/', include(urls_blog)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)