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

#mensaje = 
"""
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
        Vehiculo.contador +=1

    def info_vehiculo(self):
            print(f'La patente es {self.patente} la marca {self.marca} del año {self.anio} y el kilometraje del auto es {self.km}')
    
    def km_actual(self,km_recorrido):
        self.km += km_recorrido
        print(f'\nEl nuevo kilometraje una vez recorrido {km_recorrido} km es de {self.km} km')
    
    @classmethod
    def contador_auto(cls):
        return cls.contador
    
lista_vehiculos = []

# El menu del ecommerce
while True:
    menu = int(input(f'\nBienvenido/a a tu Automotora\n\nMenu\n\n1) Registar vehiculo\n2) Mostrar informacion del vehiculo\n3) Actualizar kilometraje\n4) Contar cuantos vehiculos existen\n5) Salir\n\nIngrese una opcion: '))
    if menu == 1:
        patente = input('Ingrese la patente del vehiculo: ')
        marca = input('Ingresa la marca del vehiculo: ')
        anio = input('Ingresa el año del vehiculo: ')
        km = int(input('Ingresa el kilometraje del vehiculo: '))
        auto = Vehiculo(patente,marca,anio,km)
        lista_vehiculos.append(auto)

        
    elif menu ==2:
        for i in lista_vehiculos:
            i.info_vehiculo()

    elif menu ==3:
        actualizar_km_patente = input('Ingrese la patente del vehiculo a actualizar el kilometraje: ')
        km_recorrido = int(input('Cuantos kilometros recorrio con el auto recientemente: '))

        if km_recorrido < 0:
            print('El kilometraje debe ser mayor a 0')
        else:
            encontrado = False
            for i in lista_vehiculos:
                if i.patente == actualizar_km_patente:
                    i.km_actual(km_recorrido)
                    encontrado = True
                    break
            if not encontrado:
                print('No existe vehiculo con esa patente')

    elif menu ==4:
        print('Cantidad de autos registrados: ',Vehiculo.contador_auto())

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
class Consulta:

    def __init__(self,hora_atencion,nombre_paciente,nombre_profesional):
        self.hora_atencion = hora_atencion
        self.nombre_paciente = nombre_paciente
        self.nombre_profesional = nombre_profesional
        self.estado = 'reservada'
        self.agendado = []

    def crear_reservas (self,lista_reserva):
        self.agendado.append(lista_reserva)
    
    def cancelar_reservas (self):
        self.estado = 'cancelada'

    def mostrar_informacion(self):
        print(f'El nombre del paciente {self.nombre_paciente.nombre_paciente} agendo la hora a las {self.hora_atencion} con {self.nombre_profesional.nombre_profesional} y el estado de la reserva esta {self.estado}')

    def contar_consultas_activas(self,lista):
        contador = 0
        for i in lista:
            if i.estado == 'reservada':
                contador +=1
        return contador


lista_reservas = []

class Paciente:

    def __init__(self,nombre_paciente):
        self.nombre_paciente = nombre_paciente

class Profesional:
    
    def __init__(self,nombre_profesional):
        self.nombre_profesional = nombre_profesional

while True:
    menu = int(input(f'\nBienvenido/a al Servicio de salud\n\nMenu\n\n1) Crear reservas\n2) Cancelar reservas\n3) Mostrar informacion\n4) Contar consultas activas\n5) Salir\n\nIngrese una opcion: '))

    if menu == 1:
        paciente = input('Ingrese su nombre: ')
        profesional = input('Ingrese el nombre del profesional: ')
        hora_atencion = input("Ingrese la hora de atención (Hora:Minuto): ")
        p1 = Paciente(paciente)
        pro1= Profesional(profesional)
        con1= Consulta(hora_atencion,p1,pro1)
        lista_reservas.append(con1)
    
    elif menu == 2:
        paciente_cancelar = input('Ingrese su nombre: ')
        encontrado = False
        for i in lista_reservas:
            if i.nombre_paciente.nombre_paciente == paciente_cancelar:
                i.cancelar_reservas()
                encontrado = True
                break
        if not encontrado:
            print('Paciente el cual quiere cancelar la hora no tiene hora reservada')    

    elif menu == 3:
        for i in lista_reservas:
            i.mostrar_informacion()

    elif menu == 4:
        if len(lista_reservas) == 0:
            print('\nDebe crear reservas antes de consultar las activas')
        else:
            print(con1.contar_consultas_activas(lista_reservas))

    elif menu ==5:
        print('\nGracias por tu visita, te esperamos pronto')
        break
    else:
        print('\nOpcion no valida, selecciona nuevamente')



# =========================================================
# FIN DE LA GUÍA
# =========================================================
