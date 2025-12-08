'''
Escriba un programa para ingresar las notas de los alumnos de un curso, pregunte al usuario cuántos datos
ingresará, a continuación le pida que ingrese las notas uno por uno, y finalmente entregue como salida
cuántas notas ingresadas son mayores que el promedio.
'''


cant_notas = int(input('Ingrese la cantidad de notas que va a registar: '))
suma = 0
datos = 0
lista_notas = []
for i in range(cant_notas):
    notas = float(input(f"Dato {i+1}: "))
    suma += notas
    lista_notas.append(notas)
promedio = suma / cant_notas       

for i in lista_notas:
    if i > promedio:
        datos +=1
print(f'{datos} datos son mayores que el promedio')
    
    
    
    
    
    
    
    
    
    
    
    
