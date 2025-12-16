
from catalogo import catalogo

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
            print('\n¡Producto agregado al carrito de compras exitosamente!')
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