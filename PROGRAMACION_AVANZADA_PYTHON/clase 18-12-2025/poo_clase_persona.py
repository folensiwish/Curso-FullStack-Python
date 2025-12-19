class Persona:
    especie = 'Homo sapiens'
    tipo_reproduccion = 'sexual'

    def __init__(self,nombre,edad,genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    
    def mostrar_atributos(self):
        print(f'Mi nombre es {self.nombre} la edad que tengo {self.edad} y mi genero es {self.genero}')
    
    def saludar(self):
        print(f'\nHola mi nombre es {self.nombre}, ¡Te Saludo!')
        
    def manejar(self):
        if self.edad >= 18:
            print('Tienes mayoria de edad puede manejar')
        else:
            print('Debe cumplir la mayoria de edad')

    @staticmethod
    def respirar():
        print('Estoy respirando oxigeno')
    
    @staticmethod
    def pensar():
        print('Estoy pensando en como hacerlo')

robin = Persona('Robinson',15,'Masculino')
robin.saludar()
robin.manejar()
robin.mostrar_atributos()
robin.respirar()
robin.pensar()

ashly = Persona('Ashly',25,'Femenino')
ashly.saludar()
ashly.manejar()
ashly.mostrar_atributos()
ashly.respirar()
ashly.pensar()