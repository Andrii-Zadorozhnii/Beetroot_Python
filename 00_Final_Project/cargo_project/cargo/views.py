import uuid

from django.db.models import Count
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models.functions import TruncDate

from django.contrib.auth.decorators import login_required


from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Customer, Company, Manager, Cargo, User

# from .forms import RegisterForm

from cargo_project.service import get_route_info
import pdb;


#   MAIN PAGE
def main_page(request):
    today = timezone.now().date()
    start_week = today - timedelta(days=6)  # включає сьогодні + 6 назад

    # Для графіка за останні 7 днів
    week_stats = (
        Cargo.objects
        .filter(created_at__date__range=(start_week, today))
        .annotate(day=TruncDate('created_at'))
        .values('day')
        .annotate(count=Count('id'))
        .order_by('day')
    )

    # Словник з днями, навіть якщо немає вантажів
    last_7_days = [(today - timedelta(days=i)) for i in reversed(range(7))]
    week_data = {str(d): 0 for d in last_7_days}
    for item in week_stats:
        week_data[str(item['day'])] = item['count']

    # Загальна кількість за поточний місяць
    first_day_of_month = today.replace(day=1)
    month_count = Cargo.objects.filter(created_at__date__gte=first_day_of_month).count()
    labels = list(week_data.keys())
    values = list(week_data.values())
    return render(request,'home/index.html', {
    'week_data': week_data,
    'month_count': month_count,
    'labels': labels,
    'values': values,
})

#   REGISTRATION /// LOGIN /// LOGOUT
def reg_view(request):
    print("click1")


    if request.method == 'POST':
        role = request.POST.get('role')
        login = request.POST.get('login')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        print('click2')

        if password == password2:
            usr = User.objects.create_user(
            role=role,
            username = login,
            email = email,
            first_name = first_name,
            last_name = last_name,
            password = password,
            )

            if role == 'manager':
                if request.method == 'POST':
                    company_name = request.POST.get('company')
                    phone = request.POST.get('phone')

                    company = Company.objects.create(
                        company_name=company_name,
                    )

                    manager = Manager.objects.create(
                        user=usr,
                        manager_phone=phone,
                        company=company
                    )

            usr = authenticate(request, username=login, password=password)
            if usr is not None:
                user_login(request, usr)
                return HttpResponseRedirect('/')
            else:
                return render(request, "account/register.html", {'error': 'Неверный логин или пароль'})

    return render(request, "account/register.html")

def login_view(request):

    if request.method == 'POST':

        login = request.POST.get('login')
        password = request.POST.get('password')

        usr = authenticate(request, username=login, password=password)

        if usr is not None:
            user_login(request, usr)
            return HttpResponseRedirect('/')
        else:
            return render(request, "account/login.html", {'error': 'Неверный логин или пароль'})

    return render(request, "account/login.html")

def logout_view(request):
    user_logout(request)
    return HttpResponseRedirect('/')

#   CARGO LIST /// ADD CARGO
@login_required
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

@login_required
def add_cargo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        description = request.POST.get('description')
        payment = request.POST.get('payment')

        # Попробуем получить дополнительные данные
        try:
            manager = Manager.objects.get(user=request.user)
            company = manager.company
            phone = manager.manager_phone
        except Manager.DoesNotExist:
            company = None
            phone = None

        # Получение информации о маршруте
        route_info = get_route_info(origin, destination)
        distance = route_info.get('distance') if route_info else None
        duration = route_info.get('duration') if route_info else None

        # Создаём новый груз
        cargo = Cargo.objects.create(
            name=name,
            origin=origin,
            destination=destination,
            description=description,
            distance=distance,
            duration=duration,
            shipment_id=str(uuid.uuid4())[:12],
            company=company,
            phone=phone,
            payment=payment,
            user=request.user
        )

        return redirect('cargo_list')  # Или другая нужная страница

    return render(request, 'cargo/add_cargo.html')

#   FUEL COUNTER
def fuel_counter(request):
    return render(request, 'fuel_counter/fuel_counter.html')

# ABOUT

def about(request):
    return render(request, 'about/about.html')




