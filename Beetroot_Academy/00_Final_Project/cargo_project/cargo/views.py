from http.client import HTTPResponse
from tkinter.font import names


from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Cargo
from .models import Customer

from cargo_project.service import get_route_info


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


def login_view(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')

        # Попытка аутентификации
        user = authenticate(request, username=login, password=password)

        if user is not None:
            user_login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, "account/login.html", {'error': 'Неверный логин или пароль'})

    return render(request, "account/login.html")

def reg_view(request):

    if request.method == 'POST':

        login = request.POST.get('login')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password2 == password:

            User.objects.create_user(username=login, password=password)


            usr = authenticate(request, username=login, password=password)

            if usr is not None:
                user_login(request, usr)
                return HttpResponseRedirect('/')
            else:
                return render(request, "account/login.html")



    return render(request, "account/register.html")

def logout_view(request):
    user_logout(request)
    return HttpResponseRedirect('/')





