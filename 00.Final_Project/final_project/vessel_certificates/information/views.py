from django.shortcuts import render

def information(request):
    return render(request, 'information/information.html')