'''
Preguntale a un usuario su nombre y su apellido y luego muestralo por pantalla con un mensaje de salud en el mensaje solo deben ir con mayuscula el nombre de la 
persona
'''

nombre= input('Ingrese su nombre y apellido: ')
nombres = nombre
nombre1, apellido = nombres.split(' ')

print(f'Hola {nombre1.upper()} {apellido}, gusto saludarte y que pases por acá.')

'''
ejercicio 1 Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en 
líneas distintas el nombre del usuario tantas veces como el número introducido.
'''

nombre = input('Ingrese su nombre: ')
numero = int(input('Ingrese un número: '))
print(f'\n{nombre}'* numero)

'''
ejercicio 2 Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene 
<n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
'''

nombre_usuario = input('Ingrese el nombre: ')
print(f'<{nombre_usuario.upper()}> tiene {len(nombre_usuario)} letras')

'''
ejercicio 3 Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos 
dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono 
sin el prefijo y la extensión.
'''

formato_telefono = input("Ingrese el numero telefonico (ej +34-913724710-56): ")
telefono = formato_telefono.split('-')
print(telefono[1])

'''
ejercicio 4 Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la 
vocal introducida en mayúscula.
'''

frase = input('Escriba una frase: ')
vocal = input('Escriba una vocal: ')
frase_final = frase.replace('a', vocal.upper() )
print(frase_final)
