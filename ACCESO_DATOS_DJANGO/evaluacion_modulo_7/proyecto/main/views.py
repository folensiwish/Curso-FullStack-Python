from django.shortcuts import render, redirect
from .models import Producto, Categoria
from django.contrib import messages

def listar_producto(request):
    productos = Producto.objects.all()
    return render(request, 'listar_producto.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        var_nombre = request.POST['nombre']
        var_precio = request.POST['precio']
        var_stock = request.POST['stock']
        var_cat_id = request.POST['categoria_id']
        
    
        if int(var_precio) <= 0:
            messages.error(request, "El precio debe ser mayor a 0")
            return redirect('crear_producto')
        
        
        Producto.objects.create( nombre=var_nombre, precio=var_precio, stock=var_stock, categoria_id=var_cat_id)
        messages.success(request, "Producto creado con éxito")
        return redirect('listar_producto')
    
    categorias = Categoria.objects.all()
    return render(request, 'formulario_producto.html', {'categorias': categorias})

#
def editar_producto(request, id):

    producto_qs = Producto.objects.filter(id=id)
    producto = producto_qs.first() 

    if not producto:
        messages.error(request, "El producto no existe")
        return redirect('listar_producto')

    if request.method == 'POST':
        var_nombre = request.POST['nombre']   
        var_precio = request.POST['precio']   
        var_stock = request.POST['stock'] 
        var_cat_id = request.POST['categoria_id'] 
    
      
        producto_qs.update(nombre=var_nombre,precio=var_precio,stock=var_stock,categoria_id=var_cat_id)
        messages.success(request, "Producto actualizado correctamente")
        return redirect('listar_producto')
    
    contexto = {
        'producto': producto, 
        'categorias': Categoria.objects.all() 
    }
    return render(request, 'formulario_producto.html', contexto)


def eliminar_producto(request, id):
    producto_qs = Producto.objects.filter(id=id)
    producto = producto_qs.first()

    if not producto:
        messages.error(request, "El producto no existe.")
        return redirect('listar_producto')

    if request.method == 'POST':
        nombre_tmp = producto.nombre
        producto_qs.delete()
        messages.success(request, f"Producto '{nombre_tmp}' eliminado con éxito.")
        return redirect('listar_producto')

    return render(request, 'confirmar_eliminacion.html', {'producto': producto})