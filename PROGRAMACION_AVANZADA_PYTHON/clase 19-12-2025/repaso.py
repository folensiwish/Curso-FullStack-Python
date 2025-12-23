"""
SUGERENCIA:
-----------
Antes de programar:
1. Identifica atributos y métodos
2. Distingue atributos de clase y de instancia
3. Dibuja la clase
4. Implementa paso a paso
5. Prueba con múltiples objetos
"""

# =========================================================
# 9. EJERCICIO 1: SISTEMA DE GESTIÓN DE VEHÍCULOS
# =========================================================
"""
CONTEXTO:
---------
Una empresa de transporte necesita administrar su flota
de vehículos.

REQUERIMIENTOS:
---------------
Cada vehículo debe tener:
- Patente
- Marca 
- Año 
- Kilometraje 

El sistema debe permitir:
- Registrar vehículos <- crear una instancia
- Mostrar información del vehículo
- Actualizar kilometraje
- Contar cuántos vehículos existen

REGLAS:
-------
- Crear una clase Vehiculo
- Usar atributos de instancia
- Usar un atributo de clase como contador
- Usar métodos de instancia
- Usar un método de clase
- Usar un método estático para validar el año
"""

mensaje = """
1 - Registrar vehículos 
2 - Mostrar información del vehículo
3 - Actualizar kilometraje
4 - Contar cuántos vehículos existen
5 - Salir
>>>: """

class Vehiculo:
    contador = 0

    def __init__(self,patente,marca,anio,km):
        self.patente = patente
        self.marca = marca
        self.anio = anio
        self.km = km

    def info_vehiculo(self):
        print(f'La marca del vehiculo es {self.marca}, la patente {self.patente} su año {self.anio} y el kilometraje {self.km}')
    
    def km_actual(self,km_recorrido):
        self.km += km_recorrido
        print(f'El nuevo kilometraje una vez recorrido {km_recorrido} km es de {self.km} km')
    
    @classmethod
    def contador_auto(cls):
        cls.contador = len()

lista_vehiculos = []
# El menu del ecommerce
while True:
    menu = int(input(f'\nBienvenido/a a tu Ecommerce\n\nMenu\n\n1) Ver catálogo de productos\n2) Buscar producto por nombre o categoría\n3) Agregar producto al carrito\n4) Ver carrito y total\n5) Vaciar carrito\n0) Salir\n\nIngrese una opcion: '))
    if menu == 1:
        patente = input('Ingrese la patente del vehiculo: ')
        marca = input('Ingresa la marca del vehiculo: ')
        anio = input('Ingresa el año del vehiculo: ')
        km = int(input('Ingresa el kilometraje del vehiculo: '))
        auto = Vehiculo(patente,marca,anio,km)
        lista_vehiculos.append(auto)
        print(lista_vehiculos)
    elif menu ==2:
        Vehiculo.info_vehiculo()
    elif menu ==3:
        agregar_producto(int(input('Ingrese el id del producto: ')), int(input('Ingrese la cantidad del producto: ')))
    elif menu ==4:
        carrito_total()
    elif menu ==5:
        print('\nGracias por tu visita, te esperamos pronto')
        break
    else:
        print('\nOpcion no valida, selecciona nuevamente')

# =========================================================
# 10. EJERCICIO 2: SISTEMA DE RESERVAS MÉDICAS
# =========================================================
"""
CONTEXTO:
---------
Un centro de salud necesita gestionar reservas de consultas.

REQUERIMIENTOS:
---------------
Cada consulta debe tener:
- Nombre del paciente
- Nombre del profesional
- Hora de atención
- Estado (reservada / cancelada)

El sistema debe permitir:
- Crear reservas
- Cancelar reservas
- Mostrar información
- Contar consultas activas


"""

# 👉 AQUÍ COMIENZA TU SOLUCIÓN
# class Consulta:
#     pass


# =========================================================
# FIN DE LA GUÍA
# =========================================================
