'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''

password = input("Ingrese su contrasena: ")
password_guardada = 'albol'

if password_guardada == password.lower():
    print('Contrasena correcta')
else:
    print('Contrasena incorrecta')

'''
ejercicio 1 Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
'''

dividendo = float(input('Ingrese el numero dividendo: '))
divisor = float(input("Ingrese el numero divisor: "))

if divisor == 0:
    print("ZeroDivisionError, no se puede dividir por cero")
else:
    if dividendo % divisor == 0:
        print(int(dividendo/divisor))
    else:
        print(dividendo/divisor)

'''
ejercicio 2 Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a $1000  mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
'''

edad = int(input("Ingrese su edad: "))
ingreso_mensual = int(input("Ingrese su ingreso mensual: "))

if edad > 16 and ingreso_mensual >= 1000:
    print("El usuario tiene que tributar")
else:
    print("El usuario no tiene que tributar")

'''
ejercicio 3 Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
'''

nombre = input("Ingrese su nombre: ").lower()
sexo = input("Ingrese su sexo m/f: ").lower()

if (nombre[0] < 'm' and sexo == 'f') or (nombre[0] > 'n' and sexo =='m'):
    print("Pertenece al grupo A")
else:
    print("Pertenece al grupo B")


'''
ejercicio 4 Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, $10
'''

edad = int(input("Ingrese su edad: "))

if edad < 4 and edad > 0:
    print('Puede entrar gratis')
elif edad >= 4 and edad <= 18:
    print("Debe pagar $5")
else:
    print("Debe pagar $10")
