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

def mostrar_catalogo():

    print('Catalogo de productos:\n')
    print(f"{'id':<5} {'nombre':<20} {'categoria':<15}{'precio':<7}") 
    print("-" * 50) 

    for llave in catalogo():
        print(f'{llave['id']:<5} {llave['nombre']:<20} {llave['categoria']:<15} ${llave['precio']:<7}\n')        



def buscar_producto (producto):
    print(f"\n{'id':<5} {'nombre':<20} {'categoria':<15}{'precio':<7}") 
    print("-" * 50)
    for i in catalogo():
        if producto in i['nombre'].lower() or producto in i['categoria'].lower():
            print(f'\n{i['id']:<5} {i['nombre']:<20} {i['categoria']:<15} ${i['precio']:<7}')
     
while True:
    menu = int(input(f'\nBienvenido/a a tu Ecommerce\n\nMenu\n\n1) Ver catálogo de productos\n2) Buscar producto por nombre o categoría\n3) Agregar producto al carrito\n4) Ver carrito y total\n5) Vaciar carrito\n0) Salir\n\nIngrese una opcion: '))
    if menu == 1:
        mostrar_catalogo()
    elif menu ==2:
        buscar_producto(input('Ingrese un nombre del producto: '))
    elif menu == 0:
        print('Gracias por tu visita')
        break
    else:
        print('Opcion no valida, selecciona nuevamanete')


