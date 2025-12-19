class Celular:
    pantalla = True
    portatil = True


    def __init__(self,modelo,touch,bateria):
        self.modelo = modelo
        self.touch = touch
        self.bateria = bateria


    def presentar_modelo(self):
        print(f'\nEl modelo del celular es {self.modelo}')

    def cargar_bateria(self,estado):
        self.bateria += estado
        print(f'El porcentaje de bateria esta en {self.bateria}')

    @staticmethod
    def encender():
        print('El telefono esta encendido')

    @staticmethod
    def subir_volumen():
        print('El volumen se subio')

cel1 = Celular('Iphone xr',True, 25)
cel1.presentar_modelo()
cel1.cargar_bateria(30)
cel1.encender()
cel1.subir_volumen()

cel2= Celular('Redmi 10', False, 75)
cel2.presentar_modelo()
cel2.cargar_bateria(25)
cel2.encender()
cel2.subir_volumen()