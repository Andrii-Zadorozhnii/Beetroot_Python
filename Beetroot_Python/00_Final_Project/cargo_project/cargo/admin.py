from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Cargo, User

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ("name", "origin", "destination", "payment", "shipment_id")
    search_fields = ("name", "origin", "destination", "shipment_id")
    list_filter = ("origin", "destination", "company")
    ordering = ("name",)
    readonly_fields = ("shipment_id",)

# Проверяем, зарегистрирована ли модель User
if admin.site.is_registered(User):
    admin.site.unregister(User)

# Регистрируем свою админку для User
@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('id', 'role', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser',)
    search_fields = ('email',)
    list_filter = ('is_staff', 'is_active', 'role',)