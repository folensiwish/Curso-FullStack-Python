'''
 van a crear 3 objetos diferentes
 un objeto auto
 un objeto gato
 un objeto casa
 le van a crear 4 atributos a cada objeto
 y 2 metodos
 despues a cada objeto le van a crear 2instancias
 cada instsancia debe tener los atributos difentes a los otros
 y mostrar lo que hacen los metodos
'''

class Auto:

    color = ''
    modelo = ''
    anho = 0
    km = 0

    def acelerar(self):
        print('El auto esta acelerando')
    
    def frenar(self):
        print('El auto esta frenando')

sedan = Auto()
sedan.color = 'gris'
sedan.modelo = 'Chevrolet Sail'
sedan.anho = 2019
sedan.km = 109000

suv = Auto()
suv.color = 'blanco'
suv.modelo = 'Nissan Qashqai'
suv.anho = 2012
suv.km = 134500

print(sedan.modelo)
print(sedan.color)
print(sedan.anho)
print(sedan.km)
sedan.acelerar()
sedan.frenar()

print('\n'+suv.modelo)
print(suv.color)
print(suv.anho)
print(suv.km)
suv.acelerar()
suv.frenar()




