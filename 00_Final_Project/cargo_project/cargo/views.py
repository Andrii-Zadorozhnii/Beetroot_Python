from tkinter.font import names

from django.shortcuts import render
from django.urls import reverse

from .models import Cargo
from .models import Customer

from cargo_project.service import get_route_info

GOOGLE_MAPS_API_KEY = 'AIzaSyCfB1EAVuIvBnDjolH6SOtuami3gaLuSNI'

def main_page(request):
    return render(request,'home/index.html')

def base(request):
    nav = [
        {"header": "Main Page", "url": reverse("home")},
        {"header": "Cargo", "url": reverse("cargo_list")},
        {"header": "Customers", "url": reverse("customers")},
        {"header": "Products", "url": reverse("products")},
    ]
    return render(request, "base.html", {"nav": nav})

def cargo_list(request):
    cargos = Cargo.objects.all()

    # Получаем уникальные значения для фильтров
    origins = Cargo.objects.values_list('origin', flat=True).distinct()
    destinations = Cargo.objects.values_list('destination', flat=True).distinct()

    # Обновляем информацию о маршруте для каждого груза
    for cargo in cargos:
        if not cargo.distance and not cargo.duration:
            route_info = get_route_info(cargo.origin, cargo.destination)
            if route_info:
                cargo.distance = route_info['distance']
                cargo.duration = route_info['duration']
                cargo.save()  # Сохраняем обновленные данные в базу

    return render(request, 'cargo/cargo.html', {
        'cargos': cargos,
        'origins': origins,
        'destinations': destinations,
    }, )

def customers(request):
    companies = Customer.objects.all()

    return render(request, 'customers/customers.html', {"companies": companies})

def products(request):
    return render(request, 'products/products.html')

