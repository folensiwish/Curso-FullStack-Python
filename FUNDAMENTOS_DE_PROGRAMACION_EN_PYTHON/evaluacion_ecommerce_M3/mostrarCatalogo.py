
from catalogo import catalogo

#Se genera una salida con columnas asignandole un ancho predeterminado para que quede alineado con los valores de los productos
def mostrar_catalogo():

    print('Catalogo de productos:\n')
    print(f"{'id':<5} {'nombre':<20} {'categoria':<15}{'precio':<7}") 
    print("-" * 50) 

    for valor in catalogo():
        print(f'{valor['id']:<5} {valor['nombre']:<20} {valor['categoria']:<15} ${valor['precio']:<7}\n')  