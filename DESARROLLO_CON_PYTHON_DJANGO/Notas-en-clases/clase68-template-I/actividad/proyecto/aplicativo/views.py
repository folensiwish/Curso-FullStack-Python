from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def perfil(request):
    nombre = 'alberto'
    correo = 'fer.albertoandres@gmail.com'   
    telefono = 951190039
    return render(request, 'perfil.html', context={
        'nombre': nombre,
        'correo': correo,
        'telefono': telefono
    })