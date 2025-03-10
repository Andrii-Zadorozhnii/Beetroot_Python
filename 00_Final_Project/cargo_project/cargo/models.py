from sys import maxunicode

from django.db import models

class Cargo(models.Model):
    name = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    distance = models.CharField(max_length=255, null=True, blank=True)  # Для хранения расстояния
    duration = models.CharField(max_length=255, null=True, blank=True)  # Для хранения времени в пути
    description = models.CharField(max_length=500, null=True, blank=True)
    shipment_id = models.CharField(max_length=20, null=True, blank=True, unique=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    payment = models.CharField(max_length=255)
    image = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.name