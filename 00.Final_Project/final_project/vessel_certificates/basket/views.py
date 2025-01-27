from django.shortcuts import render

def basket(request):
    return render(request, 'basket/basket.html')