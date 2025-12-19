class Casa:

    banhos = 0
    dormitorio = 0
    mts_construido = 0
    material = ''

    def abrir_ventanas(self):
        print('Las ventanas se abrieron')

    def prender_luces(self):
        print('Las luces se prendieron')

choza = Casa()

choza.banhos = 1
choza.dormitorio = 1
choza.mts_construido = 32
choza.material = 'Madera'

print(choza.banhos)
print(choza.dormitorio)
print(choza.mts_construido)
print(choza.material)

choza.abrir_ventanas()
choza.prender_luces()

casona = Casa()

casona.banhos = 3
casona.dormitorio = 6
casona.mts_construido = 120
casona.material = 'Hormigon'

print(f'Cantidad de baños: {casona.banhos}')
print(f'Cantidad de dormitorios: {casona.dormitorio}')
print(f'Cantodad de metros cuadrados construidos: {casona.mts_construido}')
print(f'Material usado para la construccion de la casa: {casona.material}')

casona.abrir_ventanas()
casona.prender_luces()