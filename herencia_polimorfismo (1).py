""" class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f'Hola soy {self.nombre}'

    def caminar(self):
        return f'Hola soy {self.nombre} y estoy caminandi'
    

class Estudiante(Persona): #herencia
    def __init__(self, nombre, carrera):
        super().__init__(nombre)
        self.carrera = carrera

    #polimorfismo del metodo saludar
    def saludar(self):
        return f'Hola soy {self.nombre} y estoy estiando {self.carrera}'
    
    def caminar(self):
        return f'Hola soy {self.nombre} y estoudio {self.carrera} y estoy caminandi'


p1 = Persona('David')
print(p1.saludar())

e1 = Estudiante('Guillermo', 'fullstack Python')

print(e1.saludar())
"""


class Trabajador:
    def trabajar(self):
        return 'Hola estoy trabajando'
    

class Deportista:
    def entrenar(self):
        return 'hoy estoy entranando'
    


class ProfesroEdFisica(Trabajador, Deportista):...
#averiguar que pasa con el super().__init__ aca


profe = ProfesroEdFisica()

print(profe.trabajar())
print(profe.entrenar())

