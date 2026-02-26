from django.urls import path
from actividad import views

urlpatterns = [
    path('form', views.formulario, name='formulario ')
]