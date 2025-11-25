'''
1. Entrega la edad de una persona y muestra por pantalla cuantos años tendra el 2028
'''
'''
edad = int(input("Escriba su edad: "))
anio_actual = 2025
anio_futuro = 2028

print((anio_futuro-anio_actual)+ edad)
'''
'''
2. Solicita tres notas decimales, calcula el promedio y muestralo redondeando a 1 decimal
'''
'''
nota_1 = float(input("Ingresa tu nota 1: "))
nota_2 = float(input("Ingresa tu nota 2: "))
nota_3 = float(input("Ingresa tu nota 3: "))
promedio = (nota_1 + nota_2 + nota_3) / 3

print(round(promedio, 1))
'''
'''
3. Pide la temperatura en celsius y conviertela a fahrenheit usando la formula: Fahrenheit = celsius x 1.8 + 32
'''

temperatura_celsius = int(input("Ingrese la temperatura en celsius: "))
temperatura_fahrenheit = float(temperatura_celsius * 1.8 +32)

print("La temperatura en celsius es: " , temperatura_celsius,"°C", "y la temperatura en fahrenheit es de: " , temperatura_fahrenheit,"°F")