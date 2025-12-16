'''
1) Sistema de Biblioteca

Crea un programa que permita:

Ver catálogo de libros (id, título, autor, categoría).

Buscar por título o autor.

“Pedir prestado” un libro (agregar a una lista de préstamo).

Ver libros prestados.

Devolver libro.

Salir.

📌 Debe prevenir pedir un libro que no existe o repetir uno ya prestado.
'''
'''
while True:
    menu = int(input('Bienvenido '))

    salir = input("Escribe exit para salir del programa")
    if salir == 'exit':
        print("Nos vemos luego, Adíos")
        break
'''


