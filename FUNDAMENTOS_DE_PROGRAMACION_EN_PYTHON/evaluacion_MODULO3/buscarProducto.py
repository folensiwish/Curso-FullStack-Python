
from catalogo import catalogo

#Se le pide por parametro el nombre del producto o categoria, se asigna una grilla con ancho definido para mejorar la visibilidad de la salida.
def buscar_producto (nombre_producto):
    print(f"\n{'id':<5} {'nombre':<20} {'categoria':<15}{'precio':<7}") 
    print("-" * 50)

    for i in catalogo():
        if nombre_producto in i['nombre'].lower() or nombre_producto in i['categoria'].lower():
            print(f'\n{i['id']:<5} {i['nombre']:<20} {i['categoria']:<15} ${i['precio']:<7}')