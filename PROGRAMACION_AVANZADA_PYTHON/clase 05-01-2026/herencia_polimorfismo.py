'''
EJERCICIO PRÁCTICO 1:
Crear el código fuente de un programa Python aplicando los conceptos de POLIMORFISMO, que cuente con los siguientes requerimientos:
 Debe crearse una clase llamada Gato y otra clase llamada Perro
Crear el método llamado “hablar” para clase gato que imprima el mensaje “Miau”. 
Crear el método llamado “hablar” para clase perro que imprima el mensaje “Guau!”.
Crear una función llamada “hablarMascota” fuera de la clase “Perro” que reciba como parámetro el valor de los objetos creados.
Crear los objetos gato y perro
invocar la función “hablarMascota” esperando como resultado la impresión por pantalla del método “hablar” y su distinto comportamiento según objeto.

'''

class Gato:
    
    def hablar(self):
        print('"Miau"')

class Perro:
    
    def hablar(self):
        print('"Guau!"')
'''
def hablarMascota(cat1,per1,dog2):
    print(f'El gato hace {cat1.hablar()}')
    print(f'El perro hace {per1.hablar()}')
    print(f'El perro2 hace {dog2.hablar()}')
'''
def hablarMascota(animal):
    animal.hablar()

cat = Gato()
dog = Perro()
dog2= Perro()

hablarMascota(cat)
hablarMascota(dog)
hablarMascota(dog2)



