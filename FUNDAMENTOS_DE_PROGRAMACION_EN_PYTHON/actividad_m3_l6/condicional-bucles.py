'''
1. Al ingresar un numero par cualquiera que sea del 2 al 100, este imprima en pantalla todos los
números pares siguientes, y si ingreso un número impar cualquiera sea del 1 al 99 se imprima en
pantalla todos los números impares siguientes hasta el 99.

Si ingreso el 0 o un número menor y si ingreso un número mayor al 100, el programa debe enviar un
mensaje de que no es posible realizarlo y volver a preguntar por el ingreso del número.
'''

while True:
    numero = int(input("Ingresa un numero: "))
    if numero <= 0 or numero > 100:
        print("No es posible realizarlo")
    numero +=2
    while (numero >= 2 and numero <= 100 and numero % 2 ==0) or (numero >=1 and numero <=99 and numero % 2 !=0):
            print(numero)
            numero+=2
           
    salir = input('Desea ingresar otro numero?: s/n: ').lower()
    if salir == 'n':
         break   

'''
Ejercicio 2:
Realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre
0 y 10). A continuación, debe mostrar todas las notas, la nota media, la nota más alta que ha sacado
y la menor.
'''

nota1= float(input("Ingresar tu nota: "))
nota2= float(input("Ingresar tu nota: "))
nota3= float(input("Ingresar tu nota: "))
nota4= float(input("Ingresar tu nota: "))
nota5= float(input("Ingresar tu nota: "))

if (nota1 >= 0 and nota1< 11) and (nota2 >= 0 and nota2< 11) and (nota3 >= 0 and nota3< 11) and (nota4 >= 0 and nota4< 11) and (nota5 >= 0 and nota5< 11):
    
    promedio = round((nota1+nota2+nota3+nota4+nota5)/5,1)
    lista_notas = []
    lista_notas.append(nota1)
    lista_notas.append(nota2)
    lista_notas.append(nota3)
    lista_notas.append(nota4)
    lista_notas.append(nota5)

    nota_alta = max(lista_notas)
    nota_menor = min(lista_notas)


    print(f'\nTodas las notas estan aca: \nNota 1: {nota1} \nNota 2: {nota2} \nNota 3: {nota3} \nNota 4: {nota4} \nNota 5: {nota5} \n\nNota promedio: {promedio}\nNota alta: {nota_alta}\nNota baja: {nota_menor}')
else:
    print("Debe ingresar notas que este entre el 0 y 10")

'''
Ejercicio 3:
Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga
cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para simplificarlo vamos
a suponer que febrero tiene 28 días.
'''

mes = int(input("Ingrese el numero del Mes: "))

meses = ["Enero", "Febrero", "Marzo", "Abril",
         "Mayo", "Junio", "Julio", "Agosto",
         "Septiembre", "Octubre", "Noviembre", "Diciembre"]

dias = [31, 28, 31, 30,
        31, 30, 31, 31,
        30, 31, 30, 31]

print(f'Tiene {dias[mes-1]} dias el mes de {meses[mes-1]}')





