class Gato:

    nombre = ''
    raza = ''
    color = ''
    kg = 0

    def comer(self):
        print('El gato esta comiendo')
    
    def maullar(self):
        print('Miauuuuu')

gato_feliz = Gato()

gato_feliz.nombre = 'Silvestre'
gato_feliz.raza = 'Mestizo'
gato_feliz.color = 'Negro'
gato_feliz.kg = 15

print(gato_feliz.nombre)
print(gato_feliz.raza)
print(gato_feliz.color)
print(gato_feliz.kg)

gato_feliz.comer()
gato_feliz.maullar()

gatubela = Gato()

gatubela.nombre = 'Luna'
gatubela.raza = 'Gato romano'
gatubela.color = 'naranjo con negro'
gatubela.kg = 12

print('\n'+gatubela.nombre)
print(gatubela.raza)
print(gatubela.color)
print(gatubela.kg)

gatubela.comer()
gatubela.maullar()

