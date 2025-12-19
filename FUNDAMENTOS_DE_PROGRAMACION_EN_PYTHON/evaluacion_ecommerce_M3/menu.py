
from mostrarCatalogo import mostrar_catalogo
from buscarProducto import buscar_producto
from carrito import agregar_producto, carrito_total, vaciar_carrito

# El menu del ecommerce
while True:
    menu = int(input(f'\nBienvenido/a a tu Ecommerce\n\nMenu\n\n1) Ver catálogo de productos\n2) Buscar producto por nombre o categoría\n3) Agregar producto al carrito\n4) Ver carrito y total\n5) Vaciar carrito\n0) Salir\n\nIngrese una opcion: '))
    if menu == 1:
        mostrar_catalogo()
    elif menu ==2:
        buscar_producto(input('Ingrese un nombre del producto o la categoria: ').lower())
    elif menu ==3:
        agregar_producto(int(input('Ingrese el id del producto: ')), int(input('Ingrese la cantidad del producto: ')))
    elif menu ==4:
        carrito_total()
    elif menu ==5:
        vaciar_carrito()
    elif menu == 0:
        print('\nGracias por tu visita')
        break
    else:
        print('\nOpcion no valida, selecciona nuevamente')