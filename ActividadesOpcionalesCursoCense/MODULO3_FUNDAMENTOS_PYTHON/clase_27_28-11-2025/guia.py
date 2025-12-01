
'''Guía de Ejercicios – Python (Bootcamp)
1. Verificación de mayoría de edad
Solicita al usuario su edad y muestra si es mayor o menor de edad.
'''
'''
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
'''
'''
2. Par o impar
Solicita un número entero y determina si es par o impar.
'''
'''
numero = int(input('Ingresa un numero: '))
if numero % 2 ==0:
    print('Es par')
else:
    print('Es impar')
'''
'''
3. Contador regresivo Solicita un número entero y realiza un conteo regresivo hasta 0 usando un ciclo.
'''
'''
numero = int(input('Ingresa un numero entero: '))
for i in range(numero):
    print(numero-i)
'''
'''
4. Calculadora de descuentos Pide un precio y un porcentaje de descuento, calcula el precio final.
'''
'''
precio = int(input('Ofrece un precio del producto: '))
descuento = int(input('Escribe un porcentaje descuento: '))
precio_final = precio*descuento//100

print(f'El precio final es: {precio-precio_final}')
'''
'''
5. Suma de números hasta N
Solicita un número N y calcula la suma de todos los números desde 1 hasta N.
'''
'''
numero = int(input('Escribe un numero: '))
sum = 0
for i in range(numero+1):
    sum += i
print(sum)
'''
'''
6. Contar vocales en una palabra
Pide una palabra y devuelve cuántas vocales contiene.
'''
'''
#Mi solucion 9.5/10
palabra = input('Ingresa una palabra: ').lower()
suma = 0
for i in palabra:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        suma += 1
print(f'La palabra tiene {suma} vocales')
'''
'''
#Mejora de solucion 10/10
palabra = input('Ingresa una palabra: ').lower()
suma = 0
for i in palabra:
    if i in 'aeiou':
        suma+=1
print(f'La palabra tiene {suma} vocales')
'''
'''
7. Menú interactivo
Crea un menú en consola con 3 opciones simples (por ejemplo, saludar, sumar números, salir). Debe repetirse hasta que el usuario elija 'salir'.
'''
'''
while True:
    opcion = int(input('Menu:\n1.Saludar\n2.Sumar números\n3.Salir\nIngrese alguna opcion: '))
    if opcion == 1:
        print("Saludos usuario")
    elif opcion ==2:
        num1 = float(input('Ingrese el primer numero: '))
        num2 = float(input('Ingrese el segundo numero: '))
        resultado = num1+num2
        print(f'El resultado de la suma es: {resultado:g}')
    elif opcion ==3:
        break
'''
'''
8. El número secreto, define un número secreto entre 1 y 20. El usuario debe adivinarlo indicando si el valor ingresado es mayor o menor.
'''
'''
#El numero secreto lo dejamos fuera del while porque si lo declaramos adentro la iteracion estaria asignando 15 a la variable en cada vuelta del ciclo
num_secreto = 15
while True:
    
    numero = int(input("Adivine el numero secreto, ingresando un numero entre el 1 y 20: "))
    if numero > num_secreto:
        print('El valor es mayor al numero secreto')
    elif numero < num_secreto:
        print('El valor es menor al numero secreto')
    elif numero == num_secreto:
        print('Adivinaste el numero secreto, ¡Felicidades!')
        break
'''
'''
9. Convertidor de temperatura
Pregunta al usuario si quiere convertir de Celsius a Fahrenheit o al revés y realiza la conversión.
'''
'''
convertidor = input('Ingrese Celsius si quiere converit de fahrenheit a Celsius, or Fahrenheit si quiere convertir de Celsius a Fahrenheit: ').lower()

if convertidor == 'celsius':
    celsius = float(input('Ingrese la temperatura en Fahrenheit: '))
    print(f'La conversion a temperatura Celsius es: {round((celsius-32)/1.8,1):g}° Celsius')
if convertidor == 'fahrenheit':
    fahrenheit = float(input('Ingresa la temperatura en Celsius: '))
    print(f'La conversion a temperatura Fahrenheit es: {round((fahrenheit*1.8)+32,1):g}° Fahrenheit')
'''
'''
10. Validación de contraseña
Solicita al usuario una contraseña y valida si cumple con:
- Mínimo 8 caracteres
- Al menos una mayúscula
- Al menos un número'''
'''
password = input('Ingresa una password: ')

if len(password) >= 8 and any(mayuscula.isupper() for mayuscula in password) and any(numero.isdigit() for numero in password):
    print("Validada la contraseña")
else:
    print("Valide si las password contiene minimo 8 caracteres, contenga al menos una mayuscula y un numero")
'''