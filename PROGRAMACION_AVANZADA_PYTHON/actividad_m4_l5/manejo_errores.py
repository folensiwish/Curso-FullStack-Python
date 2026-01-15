'''
Instrucciones
Crea una carpeta llamada actividad_m4_l5 y dentro de ella, un archivo llamado manejo_errores.py. En
este archivo, desarrolla lo siguiente:
1. Captura básica de errores
• Escribe un programa que pida al usuario dividir dos números.
  Utiliza try/except para capturar una división por cero y mostrar un mensaje de error amigable.
2. Múltiples excepciones
• Agrega validación para que el usuario ingrese solo números.
Usa un bloque try/except con múltiples excepciones (ZeroDivisionError, ValueError).
3. Excepciones personalizadas
• Crea una función validar_edad(edad) que lance una excepción EdadInvalidaError si la edad
es menor que 0.
Define esta excepción como clase hija de Exception.
4. Limpieza de recursos
• Simula la apertura de un archivo (puede ser un print("Abriendo archivo...")) y utiliza
finally para imprimir "Cerrando archivo..." aunque haya ocurrido un error.

Entregables
• Carpeta comprimida (.zip) que contenga:
• El archivo manejo_errores.py
• Un documento README.txt explicando:
• ¿Qué tipo de error crees que es más común en programas reales?
• ¿Por qué es importante manejar excepciones?
'''
# Ejercicio 1 y 2 implementados juntos
try: 
    num1= float(input('Ingrese el dividendo: '))
    num2= float(input('Ingrese el divisor: '))

    result = num1/num2
    print(result)

except ValueError as error:
    print(f'¡Ingrese un valor numerico!, {error}')
except ZeroDivisionError as e:
    print(f'¡No puedes dividir por cero!, {e}')

class EdadInvalidaError(Exception):

    def __str__(self) ->str:
        return f'La edad debe ser mayor a 0'

#Ejercicio 3
def validar_edad(edad):
    if edad <= 0:
        raise EdadInvalidaError()
    else:
        print(f'La edad es {edad}')

try:    
    edad = int(input('Ingresa tu edad: '))
    validar_edad(edad)

except ValueError as e:
    print(e)  
except EdadInvalidaError as error:
    print(f'El error es: {error}')

#Ejercicio 4

try:
    print('Abriendo archivo...')
    x = 10/0
except ZeroDivisionError as e:
    print(f'Problema de division de 0, error al procesar el archivo. {e}')
finally:
    print('Cerrando archivo...')