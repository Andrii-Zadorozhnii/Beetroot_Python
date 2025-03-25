from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'homework_2_html_css/index.html')
