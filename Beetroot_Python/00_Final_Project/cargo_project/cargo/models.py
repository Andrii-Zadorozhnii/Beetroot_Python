from django.db import models, migrations
import uuid
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class User(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=[('driver', 'Driver'), ('manager', 'Manager')], default='Driver')

    def __str__(self):
        return self.username
    pass

class Cargo(models.Model):
    name = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    distance = models.CharField(max_length=255, null=True, blank=True)
    duration = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    shipment_id = models.CharField(max_length=50, unique=True)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    payment = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.origin} → {self.destination})"



class Role(models.Model):
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.role


class Company(models.Model):
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name


class Manager(models.Model):
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