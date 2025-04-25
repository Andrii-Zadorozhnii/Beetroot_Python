
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('notes/', views.user_notes, name='user_notes'),
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
]
