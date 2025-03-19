from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index_1(request):
    return render(request, 'polls/index.html')