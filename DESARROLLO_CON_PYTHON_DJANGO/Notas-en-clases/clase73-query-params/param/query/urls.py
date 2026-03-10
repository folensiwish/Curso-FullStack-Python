from django.urls import path
from query import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('perfil/', views.perfil, name='perfil'),
]