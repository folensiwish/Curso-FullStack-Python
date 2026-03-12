from django.urls import path
from main import views

urlpatterns = [
    path('perfil/', views.perfil, name='perfil'),
    path('', views.home, name='home'),

]