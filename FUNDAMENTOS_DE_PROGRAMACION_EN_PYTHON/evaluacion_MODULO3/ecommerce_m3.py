#Definir el menu del ecommerce:
'''
2.1. Catálogo de productos
• Definir en el código un catálogo inicial con mínimo 5 productos.
• Cada producto debe tener:
o id (entero y único),
o nombre,
o categoría (ejemplo: "ropa", "tecnología", "hogar"),
o precio (número > 0).

Sugerencia: usar una lista de diccionarios o un diccionario donde la llave sea el id.
'''
#Definimos los productos en un diccionario dentro de una lista
def catalogo():
    productos = [
        {
            'id': 1,
            'nombre': 'Mouse Razor x86',
            'categoria': 'Tecnologia',
            'precio': 85000,
        },
        {
            'id': 2,
            'nombre': 'Parlante mlab xt',
            'categoria': 'Tecnologia',
            'precio': 73000,
        },
        {
            'id': 3,
            'nombre': 'Teclado redragon',
            'categoria': 'Tecnologia',
            'precio': 20000,
        },
        {
            'id': 4,
            'nombre': 'Audifonos JBL 204',
            'categoria': 'Tecnologia',
            'precio': 35000,
        },
        {
            'id': 5,
            'nombre': 'Pantalla HP m24',
            'categoria': 'Tecnologia',
            'precio': 125000,
        }
    ]

    return productos
#Se genera una salida con columnas asignandole un ancho predeterminado para que quede alineado con los valores de los productos
def mostrar_catalogo():

    print('Catalogo de productos:\n')
    print(f"{'id':<5} {'nombre':<20} {'categoria':<15}{'precio':<7}") 
    print("-" * 50) 

    for llave in catalogo():
        print(f'{llave['id']:<5} {llave['nombre']:<20} {llave['categoria']:<15} ${llave['precio']:<7}\n')        


#Se le pide por parametro el nombre del producto o categoria, se asigna una grilla con ancho definido para mejorar la visibilidad de la salida.
def buscar_producto (nombre_producto):
    print(f"\n{'id':<5} {'nombre':<20} {'categoria':<15}{'precio':<7}") 
    print("-" * 50)

    for i in catalogo():
        if nombre_producto in i['nombre'].lower() or nombre_producto in i['categoria'].lower():
            print(f'\n{i['id']:<5} {i['nombre']:<20} {i['categoria']:<15} ${i['precio']:<7}')

#Se genera una lista global para poder usarla en la funcion carrito_total()
carrito = []
#Entregamos por parametros la id y cantidad del producto, para luego copiar la lista y agregar la cantidad , se hizo para no modificar la lista de productos original y no verse alterado los datos para uso posterior. Luego guardamos la lista copiada en la lista carrito. 
# Para poder controlar el error creamos un booleano que me indica si el id ingresado fue encontrado el ciclo se interrumpe o sino estaria ciclando por todos los productos existentes en la lista, y creamos un if para controlar lo que no se cumple en la condicion.

def agregar_producto (identificador,cantidad):
    encontrado = False
    for i in catalogo():
        if identificador == i['id'] and cantidad > 0:
            producto = i.copy()
            producto['cantidad']=cantidad
            carrito.append(producto)
            encontrado = True
            break
    if not encontrado:
        print('\nError: no se encontró el producto por el id o la cantidad no es válida')   

#Aca se crea una variable total para almacenar la suma de los subtotales de cada producto iterado, verificamos si el carrito esta vacio si es que el usuario en el menu ingresa el 4 antes de agregar los productos.
#Creamos una salida con grilla como anteriormente, y hacemos el calculo del subtotal ademas del total del carrito.

def carrito_total():
    total = 0
    if len(carrito) == 0:
        print('\n¡Tu carrito esta vacio actualmente, agrega productos!')
    else:
        print("\nCarrito de compras")
        print(f"{'id':<5} {'nombre':<20} {'cantidad':<10} {'precioUnitario':<15} {'subtotal':<10}")
        print("-" * 70)

        for i in carrito:
            subtotal = i['precio'] * i['cantidad']
            total += subtotal
            print(f"{i['id']:<5} {i['nombre']:<20} {i['cantidad']:<10} ${i['precio']:<15} ${subtotal:<10}")

        print(f'\nTotal a pagar: ${total}')

#Verificamos que el carrito no tenga productos si el usuario presiona en el menu la opcion 5 mostrandole un mensaje indicandole el estado vacio
#Luego si no ocurre la condicion anterior se aplica el metodo clear para vaciare el carrito y monstrandole un mensaje al usuario de exito
def vaciar_carrito():
    if len(carrito) == 0:
        print('\n¡El carrito ya esta vacio, no hay productos a eliminar!')
    else:
        carrito.clear()
        print('\n¡Los productos han salido eliminados del carrito!')

# El menu del ecommerce
while True:
    menu = int(input(f'\nBienvenido/a a tu Ecommerce\n\nMenu\n\n1) Ver catálogo de productos\n2) Buscar producto por nombre o categoría\n3) Agregar producto al carrito\n4) Ver carrito y total\n5) Vaciar carrito\n0) Salir\n\nIngrese una opcion: '))
    if menu == 1:
        mostrar_catalogo()
    elif menu ==2:
        buscar_producto(input('Ingrese un nombre del producto: '))
    elif menu ==3:
        agregar_producto(int(input('Ingrese el id del producto: ')), int(input('Ingrese la cantidad del producto: ')))
    elif menu ==4:
        carrito_total()
    elif menu ==5:
        vaciar_carrito()
    elif menu == 0:
        print('\nGracias por tu visita, te esperamos pronto')
        break
    else:
        print('\nOpcion no valida, selecciona nuevamente')


