from django.shortcuts import render, redirect
from .models import Libro

# Create your views here.

def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'listar_libros.html', {'libros': libros})

def crear_libro(request):
    if request.method == 'POST':
        v_titulo = request.POST['titulo']
        v_autor = request.POST['autor']
        v_fecha = request.POST['fecha_publicacion']
        Libro.objects.create(titulo=v_titulo,autor=v_autor,fecha_publicacion=v_fecha)
        return redirect('listar_libros')
        
    return render(request, 'formulario_libro.html')

def editar_libro(request, id):
    libro_queryset = Libro.objects.filter(id=id)

    if request.method == 'POST':
        v_titulo = request.POST['titulo']
        v_autor = request.POST['autor']
        v_fecha = request.POST['fecha_publicacion']

      
        libro_queryset.update(titulo=v_titulo, autor=v_autor, fecha_publicacion=v_fecha)
        return redirect('listar_libros')

    contexto = {
        'libro': libro_queryset.first() 
    }
    return render(request, 'formulario_libro.html', contexto)

def eliminar_libro(request, id):
    libro_queryset = Libro.objects.filter(id=id)
    libro = libro_queryset.first()

    if libro is None:
        return redirect('listar_libros')

    if request.method == 'POST':
        libro_queryset.delete()
        return redirect('listar_libros') 
    
    return render(request, 'confirmacion_eliminacion.html', {'libro': libro})