# Guia de Ejercicios Python - Nivel Intermedio
# ---------------------------------------------------------
# Cada ejercicio está descrito dentro de comentarios.
# Los estudiantes deben escribir el código debajo de cada enunciado.

###############################################################
# 1) SISTEMA DE GESTIÓN DE HÉROES Y VILLANOS
# -------------------------------------------------------------
# Crea un sistema donde existan héroes y villanos.
# Estructura inicial:

# villanos = [
#     {"nombre": "Sombrío", "fuerza": 70, "velocidad": 40},
#     {"nombre": "Vortéx", "fuerza": 55, "velocidad": 95}
# ]

#
# Tareas:
# 1. Permitir al usuario agregar un héroe o un villano nuevo (con nombre, fuerza y velocidad). GUARDAR -> lista_vacia.append('elemento') 

# 2. Crear una funcionalidad que determine el ganador entre cualquier héroe y villano.
#    El ganador se define por la suma: poder_total = fuerza + velocidad.
# 3. Simular una batalla: el usuario elige un héroe y un villano por nombre y el programa indica el ganador. EXTRAER -> con un for !!!!!!

# 4. Mostrar un ranking ordenado de mayor a menor poder de todos los personajes.
'''
villano = [
    {"nombre": "Sombrío", "fuerza": 70, "velocidad": 40},
    {"nombre": "Vortéx", "fuerza": 55, "velocidad": 95}
]

heroe = []

villano_dic = {}
heroe_dic = {}
agregar_psj = input('Desea agregar un villano o heroe: ').lower()

if agregar_psj == 'villano':
    villano_dic["nombre"] = input("Nombre del heroe: ")
    villano_dic["fuerza"] = int(input("Ingrese la fuerza: "))
    villano_dic["velocidad"] = int(input("Ingrese la velocidad: "))
    villano.append(villano_dic)
elif agregar_psj == 'heroe':
   heroe_dic["nombre"] = input("Nombre del heroe: ")
   heroe_dic["fuerza"] = int(input("Ingrese la fuerza: "))
   heroe_dic["velocidad"] = int(input("Ingrese la velocidad: "))
   heroe.append(heroe_dic)
else:
    print("Ingresa una opcion valida heroe/villano")

ingrese_heroe = input('Ingresa un hero para combatir: ')
ingrese_villano = input('Ingrese un villano para combatir: ')


for villain ,hero in zip(villano,heroe):
    if ingrese_villano in villain['nombre'] and ingrese_heroe in hero['nombre']:
        print(ingrese_villano, ingrese_heroe)
'''        
        
    





###############################################################
# 2) SIMULADOR DE TIENDA CON INVENTARIO DINÁMICO
# -------------------------------------------------------------
# Usar un diccionario como inventario:
# inventario = {
#     "manzana": 30,
#     "pan": 15,
#     "agua": 50
# }
#
# Tareas:
# 1. Permitir agregar productos con su cantidad.
# 2. Permitir vender productos (restar cantidad), validando que exista y que haya stock suficiente.
# 3. Si la cantidad queda en 0, eliminar automáticamente el producto.
# 4. Mostrar un resumen final del inventario, el total de productos vendidos y el desglose por artículo.

inventario = {
    "manzana": 30,
    "pan": 15,
    "agua": 50
}

while True:

    menu = int(input('\nMenu de la tienda\n\n1)Agregar productos con su cantidad\n2)Vender productos\n3)Resumen final del inventario\n0) Salir\nIngrese su opcion: '))

    if menu == 1:
        producto = input('Ingresa un producto: ').lower()
        cant_producto = int(input('Ingresa una cantidad: '))
        for i,k in inventario.items():
            if producto == i:
                inventario[i] = k + cant_producto
        inventario[producto] = cant_producto
    
    if menu == 2:
        '''
        ¿Qué entra? (inputs)

        ¿Qué sale? (outputs)

        ¿Qué cambia? (estado)

        ¿Qué se repite? (bucles)

        ¿Qué se decide? (condiciones)
        '''
        encontrado = False
        vender_producto = input('Elige el producto a vender: ').lower()

        cant_venta = int(input('Ingrese la cantidad de producto en venta: '))
        for i,k in inventario.items():
            if vender_producto == i and k >= cant_venta:
                inventario[i] = k - cant_venta
                encontrado = True
            if k - cant_venta == 0:
                del inventario[i]      
                break
                     
        if not encontrado:
            print('\nEl producto es inexistente o no hay stock suficiente')
        print(inventario)
    if menu == 3:
        
    if menu == 0:
        break






###############################################################
# 3) SISTEMA DE ENCUESTAS CON ANÁLISIS ESTADÍSTICO
# -------------------------------------------------------------
# El programa debe recoger opiniones sobre un servicio.
# Las preguntas serán:
# - Calidad (1 a 7)
# - Rapidez (1 a 7)
# - Amabilidad (1 a 7)
#
# Tareas:
# 1. Permitir almacenar respuestas de varios encuestados (mínimo 5). Cada respuesta es un diccionario.
# 2. Calcular el promedio de cada criterio.
# 3. Identificar cuál criterio obtuvo la mejor valoración promedio.
# 4. Identificar al encuestado con mejor promedio global.
# 5. Mostrar un reporte final con toda la información.


###############################################################
# 4) JUEGO DEL DRAGÓN Y EL TESORO
# -------------------------------------------------------------
# El jugador inicia con 100 puntos de vida y un inventario vacío.
# Existen tres acciones posibles por turno:
# - "explorar": puede encontrar oro, un objeto, o sufrir daño.
# - "descansar": recupera vida.
# - "huir": termina el juego.
#
# Tareas:
# 1. Simular al menos 7 turnos o hasta que el jugador llegue a 0 de vida.
# 2. Utilizar listas y diccionarios para registrar objetos encontrados.
# 3. Después de cada turno, mostrar el estado del jugador.
# 4. Al finalizar, generar un resumen del recorrido (vida final, objetos obtenidos y total de oro).


###############################################################
# 5) MINI GESTOR DE BIBLIOTECA
# -------------------------------------------------------------
# La biblioteca parte con esta estructura:
# libros = [
#     {"titulo": "1984", "autor": "George Orwell", "prestado": False},
#     {"titulo": "Fundación", "autor": "Isaac Asimov", "prestado": False},
# ]
#
# Tareas:
# 1. Permitir agregar nuevos libros.
# 2. Permitir marcar un libro como prestado o devuelto.
# 3. Generar una lista de los libros disponibles y otra de los prestados.
# 4. Crear un buscador por título que ignore mayúsculas/minúsculas.
# 5. Mostrar un resumen final con totales y listados.


###############################################################
# 6) SISTEMA DE TORNEO DE CARRERAS
# -------------------------------------------------------------
# Recibes una lista de corredores:
# corredores = [
#     {"nombre": "Luna", "velocidad": 8, "resistencia": 6},
#     {"nombre": "Kai", "velocidad": 7, "resistencia": 9},
#     {"nombre": "Rex", "velocidad": 9, "resistencia": 5}
# ]
#
# Fórmula de rendimiento:
# rendimiento = velocidad * 0.6 + resistencia * 0.4
#
# Tareas:
# 1. Permitir agregar nuevos corredores.
# 2. Simular una carrera: calcular rendimiento para cada participante.
# 3. Ordenar y mostrar el podio (1°, 2°, 3°).
# 4. Permitir al usuario buscar un corredor y mostrar su rendimiento.
# 5. Generar un ranking final completo.


# Fin del archivo

