
from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title: str = models.CharField(max_length=200)
    content: str = models.TextField()
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)
    author: User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title