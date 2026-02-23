from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def perfil(request):
    nombre = 'Alberto'
    edad = 28
    profesiones = ['Ingeniero en informatica','Dj']
    tipo_usuario = 'admin'
    return render(request, 'perfil.html', context={
        'nombre':nombre,
        'edad':edad,
        'profesiones':profesiones,
        'tipo_usuario':tipo_usuario,
    })
