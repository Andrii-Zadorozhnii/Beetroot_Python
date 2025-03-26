from django.contrib import admin
from .models import Cargo

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ("name", "origin", "destination", "payment", "shipment_id")  # Поля для отображения
    search_fields = ("name", "origin", "destination", "shipment_id")  # Поиск по этим полям
    list_filter = ("origin", "destination", "company")  # Фильтры в админке
    ordering = ("name",)  # Сортировка
    readonly_fields = ("shipment_id",)  # Поля, которые нельзя редактировать
