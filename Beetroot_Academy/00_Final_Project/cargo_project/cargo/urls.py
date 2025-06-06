from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page, name='home'),
    path('fuel_counter/', views.fuel_counter, name='fuel_counter'),
    path('cargo/', views.cargo_list, name='cargo_list'),
    path('login/', views.login_view, name='login'),
    path('register/', views.reg_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
path('add_cargo/', views.add_cargo, name='add_cargo'),
]