from django.shortcuts import render

def company(request):
    return render(request, 'company/company.html')