from django.shortcuts import render

def contacts(request):
    return render(request, 'contacts/contacts.html')