'''
Pedir el usuario que ingrese un numero, dependiendo el numero ingresado se debe imprimir el '*' desde el principio hasta el numero ingresado.
'''
'''
numero = int(input("Ingrese un numero: "))

for i in range(numero):
    print("*"*(i+1))
'''
'''
ejercicio. 1 Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''
'''
numero = int(input("Ingrese un numero positivo: "))

for i in range(numero+1):
    if i % 2 != 0:
        impar = i
        print(impar , end=',')
'''     
'''
ejercicio 2 Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
'''
'''
for i in range(1,11):
    for j in range(1,11):
        resultado = i*j
        print(f'{i}*{j} = {resultado}')
'''
'''
ejercicio 3 Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
'''
'''
password ='python'

while True:
    password_guardada = input("Ingrese la contrasena correcta: ").lower()
    if password_guardada == password:
        print('Password correcta')
        break
'''
'''
ejercicio 4 Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
'''

palabra = input('Ingese una palabra: ')

for i in palabra[::-1]:
    print(i)