from django.shortcuts import render

from .models import Notes

# Create your views here.


def home(request):
    notes = Notes.objects.all()
    return render(request, 'homework_3_ORM/index.html', {'notes': notes})