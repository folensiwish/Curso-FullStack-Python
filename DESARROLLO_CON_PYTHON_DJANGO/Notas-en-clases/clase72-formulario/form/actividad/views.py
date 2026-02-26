from django.shortcuts import render
from datetime import datetime

# Create your views here.

def formulario(request):
    if request.method == 'GET':
        return render(request, 'formulario.html')
    else:
        nombre = request.POST['nombre']
        email = request.POST['email']

        with open('datos.txt', 'a', encoding='utf-8') as archivo:
            archivo.write(f'Nombre:{nombre}, Email:{email}, Hora:{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n')
            archivo.closed

        return render(request, 'formulario.html', {'mensaje':'Has enviado el formulario'})