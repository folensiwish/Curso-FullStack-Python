'''
vas a crear 3clases
cada clase debe tener 2 atributos de clase y 3 atributos de instancia
cada clase debe tener 2 metodos estatidos y 2 metodos de instancia
cree 2 instancias de cada clase y muestr los atributos y los metodos
'''

class Auto:

    ruedas = 4
    freno_de_mano = True

    def __init__(self,color,modelo,km_ini,km_final):
        self.color = color
        self.modelo = modelo
        self.km_inicial = km_ini
        self.km_final = km_final
        
    
    def recorrido(self,kilometraje):
        self.km_final = self.km_inicial + kilometraje

    def mostrar_atributos(self):
        print(f'El modelo del auto es: {self.modelo} su color es {self.color} km incial {self.km_inicial} y el km con el que termino el recorrido {self.km_final}')

    @staticmethod
    def encender_motor():
        print('\nEl auto esta encendido')
    
    @staticmethod
    def apagar_motor():
        print('El auto esta apagado')

sedan = Auto('Rojo','Chevrolet Sail',129000,0)
sedan.encender_motor()
sedan.recorrido(10000)
sedan.apagar_motor()
sedan.mostrar_atributos()

suv = Auto('blanco','Nissan Qashqai',133000,0)
suv.encender_motor()
suv.recorrido(50000)
suv.apagar_motor()
suv.mostrar_atributos()

