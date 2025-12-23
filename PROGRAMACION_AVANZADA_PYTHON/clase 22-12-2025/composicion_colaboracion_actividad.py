"""
===============================================
EJERCICIOS POO: COMPOSICIÓN Y COLABORACIÓN
Curso: Programación en Python
===============================================

Instrucciones generales:
- Lee atentamente cada enunciado.
- Implementa las clases solicitadas.
- Respeta los nombres de clases y métodos.
- Al final de cada ejercicio, prueba tu solución
  creando objetos y mostrando resultados por pantalla.
"""


# =================================================
# EJERCICIO 1: SISTEMA DE ATENCIÓN MÉDICA
# Tema: COMPOSICIÓN
# =================================================

"""
CONTEXTO:
Se desea modelar un sistema simple de atención médica.
Un Paciente tiene un Historial Médico que almacena
diagnósticos y tratamientos.

IMPORTANTE:
- El historial médico NO debe existir sin el paciente.
- El historial se crea dentro de la clase Paciente.
Esto es un ejemplo de COMPOSICIÓN.


# 1) Crea la clase HistorialMedico
# Atributos:
# - diagnosticos (lista)
# - tratamientos (lista)
#
# Métodos:
# - agregar_diagnostico(diagnostico)
# - agregar_tratamiento(tratamiento)
# - mostrar_historial()


class HistorialMedico:

    def __init__(self):
        self.diagnostico = []
        self.tratamiento = []
    
    def agregar_diagnostico(self, diagnostic):
            self.diagnostico.append(diagnostic)

    def agregar_tratamiento(self,trata):
            self.tratamiento.append(trata)

    def mostrar_historial(self):
        print('Historial Clinico: ')
        for i in self.diagnostico:
            print(i)
        print('Tratamiento: ')
        for j in self.tratamiento:
            print(j)
'''           
h1 = HistorialMedico()
h1.agregar_diagnostico('Dolor de cuerpo')
h1.agregar_diagnostico('Dolor de cabeza')
h1.agregar_tratamiento('Ibuprofeno cada 8 horas')
h1.agregar_tratamiento('Paracetamol cada 8 horas')
h1.mostrar_historial()
'''

# 2) Crea la clase Paciente
# Atributos:
# - nombre
# - edad
# - historial (instancia de HistorialMedico)
#
# Métodos:
# - mostrar_info()


class Paciente:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.historial = HistorialMedico()
    
    def mostrar_info(self):
        print(f'El nombre del paciente es {self.nombre} su edad {self.edad} años')
        print(self.historial.mostrar_historial())


# 3) PRUEBAS (descomenta cuando tengas tu solución)

paciente1 = Paciente("Juan Pérez", 45)
paciente1.historial.agregar_diagnostico("Hipertensión")
paciente1.historial.agregar_diagnostico("Diabetes tipo 2")
paciente1.historial.agregar_tratamiento("Medicamento A")

paciente1.mostrar_info()
"""

# =================================================
# EJERCICIO 2: SISTEMA DE PEDIDOS
# Tema: COLABORACIÓN ENTRE CLASES
# =================================================

"""
CONTEXTO:
Se desea modelar un sistema de pedidos para una tienda.
Un Pedido trabaja con un Cliente y varios Productos.

IMPORTANTE:
- Cliente y Producto pueden existir de forma independiente.
- Pedido solo USA estas clases.
Esto es un ejemplo de COLABORACIÓN.
"""

# 1) Crea la clase Producto
# Atributos:
# - nombre
# - precio
#
# Métodos:
# - mostrar_info()


class Producto:
    
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        print(f'El nombre del producto: {self.nombre}')
        return self.precio


# 2) Crea la clase Cliente
# Atributos:
# - nombre
#
# Métodos:
# - mostrar_info()


class Cliente:
    
    def __init__(self,nombre):
        self.nombre = nombre
    
    def mostrar_info(self):
        return self.nombre


# 3) Crea la clase Pedido
# Atributos:
# - cliente (instancia de Cliente)
# - productos (lista de Producto)
#
# Métodos:
# - agregar_producto(producto)
# - calcular_total()
# - mostrar_resumen()


class Pedido:
    
    def __init__(self,cliente):
        self.cliente = cliente
        self.productos = []

    def agregar_producto(self,producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0
        for i in self.productos:
            total += i.precio
 
        return total
    
    def mostrar_resumen(self):
        print(f'El nombre del cliente es {self.cliente.mostrar_info()},')
        for i in self.productos:
            print(f'El {i.nombre} cuesta ${i.precio}')
        
        print(f'Total a pagar: ${self.calcular_total()}')

#4) PRUEBAS (descomenta cuando tengas tu solución)


producto1 = Producto("Teclado", 15000)
producto2 = Producto("Mouse", 8000)

cliente1 = Cliente("María González")

pedido1 = Pedido(cliente1)
pedido1.agregar_producto(producto1)
pedido1.agregar_producto(producto2)

pedido1.mostrar_resumen()


# =================================================
# PREGUNTAS DE REFLEXIÓN
# =================================================

"""
1) ¿Por qué el HistorialMedico es un ejemplo de composición?
        Porque estan correlacionados con dependencia, significa que los 2 funcionan en conjunto y no por separado. Además de como se utilizar el objeto como atributo, directamente desde los atributos de la clase 'REINA'
2) ¿Puede un Producto existir sin un Pedido? ¿Por qué?
        Porque se relacionan de manera independiente un objeto con el otro, no existe correlacion de dependencia por lo tanto pueden existir sin la necesidad del otro
3) ¿Qué diferencia principal observas entre ambos ejercicios?
        Tecnicamente, la manera en como se acceden los atributos de las otras clases, se hace mas simplificado tener directamente el objeto en los atributos que tener que invocar los atributos a traves de parametros.
"""

