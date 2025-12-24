'''
1. Exploración teórica
Escribe en comentarios (#) respuestas a las siguientes preguntas:
• ¿Qué es la programación orientada a objetos?
    Es una forma de programar donde el programa se arma usando objetos. Cada objeto representa algo real o lógico y tiene datos y acciones que puede hacer.

• ¿En qué se diferencia de la programación estructurada?
    En la programación estructurada todo se hace con funciones y pasos ordenados. En cambio, en la programación orientada a objetos se agrupa la información con las funciones dentro de un mismo objeto, lo que hace el código más ordenado y fácil de entender.

• Menciona un ejemplo de la vida cotidiana donde se vea reflejado el concepto de objeto. 
    Un celular es un objeto, tiene datos como marca y modelo, y puede hacer acciones como llamar, sacar fotos o enviar mensajes.
'''

#2
class Perro:

    def __init__(self,nombre,edad,raza):
        self._nombre = nombre
        self._edad = edad
        self._raza = raza

    @staticmethod
    def ladrar():
        print('¡Guau!')

p1 = Perro('Pepito',5, 'Kiltro')
p1.ladrar()

'''
3. Diferenciar conceptos
• En comentarios, explica la diferencia entre:
• Clase, instancia y objeto:
    -Una clase es una plantilla que define cómo será algo. 
    -Una instancia es cuando usamos ese molde para crear algo concreto 
    -El objeto es ese algo creado a partir de la clase y que ya existe en el programa.

• Atributo y estado
    -Un atributo es una característica que tiene un objeto, como nombre o edad.
    -El estado es el valor que tienen esos atributos en un momento determinado.

• Método y comportamiento
    -Un método es una función que pertenece a una clase.
    -El comportamiento es lo que el objeto puede hacer usando esos métodos.
'''

#4
class Perro:

    def __init__(self,nombre,edad,raza):
        self._nombre = nombre
        self._edad = edad
        self._raza = raza

    @staticmethod
    def ladrar():
        print('¡Guau!')
    
    def mostrar_info(self):
        print(f'El nombre es {self._nombre} la edad que tiene {self._edad} años y la raza del perrito es {self._raza}')

p1 = Perro('Pepito',5, 'Kiltro')
p1.ladrar()
p1.mostrar_info()

'''
Comenta brevemente qué significa la abstracción y cómo se relaciona con este ejemplo:

    -La abstracción significa mostrar solo la información importante de un objeto y ocultar los detalles internos.
En este ejemplo, el método mostrar_info() permite ver el estado del perro sin necesidad de acceder directamente a sus atributos internos.
'''