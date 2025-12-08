'''
Ejercicio practico 1:

Escribir un progama que almecene las asignaturas del curso, Matematicas, fisica, quimica, historia y lengueaje en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir
'''
'''
asignaturas = ['Matematica', 'Fisica', 'Quimica', 'Historia', 'Lenguaje']

repetir = []
for i in asignaturas:
    nota = float(input(f'Dime que nota tuviste en la asignatura {i}: '))
    if nota < 4:
        repetir.append(i)
print(f'Debe repetir las siguientes asignaturas: {repetir}')
'''
'''
Ejercicio pratico 2:
Escribir un proigrama que cree un diccionario y lo vaya llenando con informacion sobre una persona (por ejemplo nombre,edad,sexo,telefono,correo electronico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse 
'''
'''
diccionario = {}

while True:
    llave = input(f'Ingrese una clave: ')
    valor = input(f'Ingrese su valor: ')
    diccionario[llave] = valor
    print(diccionario)

    salir = int(input('Si desea seguir agregando informacion ingrese 1, si desea salir ingrese 0: '))
    if salir ==0:
        break
'''
'''
ejercicio 1: Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
'''
'''
divisa = {
    'Euro':'€', 
    'Dollar':'$', 
    'Yen':'¥'
}
moneda = input('Ingrese la divisa deseada: ').capitalize()
if moneda in divisa:
    print(divisa[moneda])
else:
    print('Divisa no esta en el diccionario')
'''


'''
ejercicio 2: Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
'''

'''
ejerccio 3 Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
'''
'''
palabra = input('Ingrese una palabra: ').lower()
a = 0
e = 0
i = 0
o = 0
u = 0
for vocales in palabra:
    if vocales == 'a':
        a+=1
    elif vocales == 'e':
        e+=1
    elif vocales == 'i':
        i+=1
    elif vocales == 'o':
        o+=1
    elif vocales == 'u':
        u+=1
print(f'La letra "a" se repite {a} veces\nLa letra "e" se repite {e} veces\nLa letra "I" se repite {i} veces\nLa letra "O" se repite {o} veces\nLa letra "U" se repite {u} veces')        
'''
'''
ejercicio 4 Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica
'''
'''
import statistics
muestra_numeros = input('Ingrese una muestra de numeros separados por comas: ')
lista_num = muestra_numeros.split(',')

lista_float = []
sum=0

for i in lista_num:
    sum +=float(i)
    lista_float.append(float(i))
desviacion_estandar = statistics.stdev(lista_float)
print(f'La media es: {sum/len(lista_num)} y la desviacion tipica es: {desviacion_estandar}')
'''






