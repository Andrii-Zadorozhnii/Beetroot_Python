from django.shortcuts import render
from .models import Cargo
from cargo_project.service import get_route_info

GOOGLE_MAPS_API_KEY = 'AIzaSyCfB1EAVuIvBnDjolH6SOtuami3gaLuSNI'


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

    return render(request, 'cargo.html', {
        'cargos': cargos,
        'origins': origins,
        'destinations': destinations,
    })