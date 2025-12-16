
from catalogo import catalogo

#Se genera una salida con columnas asignandole un ancho predeterminado para que quede alineado con los valores de los productos
def mostrar_catalogo():

    print('Catalogo de productos:\n')
    print(f"{'id':<5} {'nombre':<20} {'categoria':<15}{'precio':<7}") 
    print("-" * 50) 

    for llave in catalogo():
        print(f'{llave['id']:<5} {llave['nombre']:<20} {llave['categoria']:<15} ${llave['precio']:<7}\n')  