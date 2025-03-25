from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=30)

class Notes(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    reminder = models.DateTimeField("date reminder")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="notes")


