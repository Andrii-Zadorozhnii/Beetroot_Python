from django.contrib import admin
from .models import Cargo

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ("name", "origin", "destination", "payment", "shipment_id")
    search_fields = ("name", "origin", "destination", "shipment_id")
    list_filter = ("origin", "destination", "company")
    ordering = ("name",)
    readonly_fields = ("shipment_id",)