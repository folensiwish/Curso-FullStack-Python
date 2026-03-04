from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']    
        return render(request, 'home.html', context={
        'mensaje':'El formulario a sido enviado exitosamente',
        'nombre': nombre,
        'email': email                                          
        })
    else:
        return render(request, 'home.html')