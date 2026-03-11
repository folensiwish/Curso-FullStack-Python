from django.urls import path
from main import views

urlpatterns = [
    path('contacto/', views.contacto, name='contacto')
]