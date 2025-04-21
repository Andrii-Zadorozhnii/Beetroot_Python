from django.db import models, migrations
import uuid
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=[('driver', 'Driver'), ('manager', 'Manager')], default='Driver')

    def __str__(self):
        return self.username
    pass

User = get_user_model()


class Cargo(models.Model):
    name = models.CharField(max_length=255) # назва вантажу
    origin = models.CharField(max_length=255)  # місце відправлення
    destination = models.CharField(max_length=255) # місце доставки
    distance = models.CharField(max_length=255, null=True, blank=True)
    duration = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    shipment_id = models.CharField(max_length=50, unique=True)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    payment = models.DecimalField(max_digits=10, decimal_places=2)
    truck = models.CharField(max_length=100)
    currency = models.CharField(max_length=3)
    payment_method = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.origin} → {self.destination})"

    def save(self, *args, **kwargs) -> None:
        # Если у груза не указана компания или телефон, пробуем получить их из менеджера
        if not self.company or not self.phone:
            try:
                manager = Manager.objects.get(user=self.user)
                if not self.company:
                    self.company = manager.company
                if not self.phone:
                    self.phone = manager.manager_phone
            except Manager.DoesNotExist:
                pass  # Пользователь не является менеджером, пропускаем

        # Автоматическая генерация shipment_id, если он не указан
        if not self.shipment_id:
            import uuid
            self.shipment_id = str(uuid.uuid4())[:12]

        super().save(*args, **kwargs)

class Role(models.Model):
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.role


class Company(models.Model):
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name


class Manager(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    manager_phone = models.CharField(max_length=255)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.manager_phone


class Customer(models.Model):
    id = models.BigIntegerField(primary_key=True)  # Указываем, что это ключ
    customer_name = models.CharField(max_length=255)
    customer_description = models.CharField(max_length=255)
    customer_location = models.CharField(max_length=255)
    customer_location_url = models.CharField(max_length=255, null=True)
    customer_web_site = models.CharField(max_length=255, null=True)
    customer_logo = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.customer_name