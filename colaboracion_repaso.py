'''
🟢 NIVEL BÁSICO
🟢 Ejercicio 1: Persona – Dirección
Objetivo: entender objeto dentro de objeto
Enunciado

Crea las clases:

Dirección
atributos: calle, numero
método: mostrar()

Persona
atributos: nombre, direccion (instancia de Dirección)
método: mostrar_info()

Reglas
La Dirección se crea fuera y se pasa a Persona.
Persona debe usar el método de Dirección.
'''
'''
class Direccion:

    def __init__(self,calle,numero):
        self.calle = calle 
        self.numero = numero
    
    def mostrar(self):
        print(f'La calle se llama {self.calle} y el numero {self.numero}')

class Persona:

    def __init__(self,nombre,direccion):
        self.nombre = nombre
        self.direccion = direccion
    
    def mostrar_info(self):
        print(f'El nombre de la persona es {self.nombre}')
        self.direccion.mostrar()

dir1 = Direccion('San jose','1726')
p1= Persona('Alberto',dir1)
p1.mostrar_info()

'''

'''
🟢 Ejercicio 2: Libro – Autor
Objetivo: usar atributos de otra clase
Enunciado

Clases:
Autor
atributos: nombre
método: mostrar()

Libro
atributos: titulo, autor (instancia de Autor)
método: mostrar_info()
'''
'''
class Autor:

    def __init__(self,nombre):
        self.nombre = nombre
    
    def mostrar(self):
        print(f'El nombre del autor es {self.nombre}')
    
class Libro:

    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
    
    def mostrar_info(self):
        print(f'El titulo del libro es {self.titulo}')
        self.autor.mostrar()

a1 = Autor('Alberto')
l1= Libro('Principito',a1)
l1.mostrar_info()
'''

'''
🟡 NIVEL BÁSICO + LISTAS
🟡 Ejercicio 3: Curso – Estudiante
Objetivo: lista de objetos
Enunciado

Clases:
Estudiante
atributos: nombre
método: mostrar()

Curso
atributos: nombre, estudiantes (lista de Estudiante)
métodos:
agregar_estudiante(estudiante)
mostrar_estudiantes()
'''

class Estudiante:

    def __init__(self,nombre):
        self.nombre = nombre
    
    def mostrar(self):
        return self.nombre

class Curso:

    def __init__(self,nombre):
        self.nombre = nombre
        self.estudiantes = []
    
    def agregar_estudiantes(self,estudiante):
        self.estudiantes.append(estudiante)
    
    def mostrar_estudiantes(self):
        print(f'El nombre del curso es {self.nombre}')
        for i in self.estudiantes:
            print(i.mostrar())



e1=Estudiante('Alberto')
e2=Estudiante('Ashly')
c1=Curso('Taller Ingles')
c1.agregar_estudiantes(e1)
c1.agregar_estudiantes(e2)
c1.mostrar_estudiantes()
