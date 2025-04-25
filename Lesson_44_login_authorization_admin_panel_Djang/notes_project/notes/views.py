from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .models import Note


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Перенаправлення після успішного входу
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')  # Перенаправлення після виходу



@login_required
def user_notes(request):
    notes = Note.objects.filter(author=request.user)
    return render(request, 'user_notes.html', {'notes': notes})

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, author=request.user)
    if request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        return redirect('user_notes')
    return render(request, 'edit_note.html', {'note': note})

def home(request):
    return render(request, 'home.html')

@login_required
@csrf_protect
def create_note(request):
    """Створення нової нотатки"""
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Note.objects.create(
                title=title,
                content=content,
                author=request.user
            )
            return redirect('user_notes')
    return render(request, 'create_note.html')