"""
URL configuration for vessel_certificates project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from basket.views import basket
from catalog.views import catalog
from company.views import company
from contacts.views import contacts
from information.views import information
from main_page.views import main_page
from news.views import news
from products.views import products
from service.views import services


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name=''),
    path('catalog/', catalog, name='catalog'),
    path('contacts/', contacts, name='contacts'),
    path('products/', products, name='products'),
    path('services/', services, name='services'),
    path('news/', news, name='news'),
    path('basket/', basket, name='basket'),
    path('company/', company, name='company'),
    path('information/', information, name='information'),
]
