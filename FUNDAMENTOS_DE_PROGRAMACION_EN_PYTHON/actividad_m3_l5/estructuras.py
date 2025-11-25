'''
1. Crear estructuras
Declara una variable de cada una de las siguientes estructuras de datos con al menos 3 elementos cada una:
• Lista (list)
• Tupla (tuple)
• Conjunto (set)
• Diccionario (dict)
'''
#La diferencia puede ser la flexibilidad y accesibilidad a los datos.
estructura_lista = ['manzana','naranja','pomelo']
estructura_tupla = ('puerta','ventana','pared')
estructura_set = {'manzana','uva','pera'}
estructura_diccionario = {
    'nombre':'Alberto',
    'edad': 27,
    'ciudad': 'Santiago'
}
#print(estructura_lista,estructura_tupla,estructura_set,estructura_diccionario)

'''
2. Acceder a elementos
• Imprime el segundo elemento de la lista.
• Imprime una clave y su valor desde el diccionario.
• Explica con comentarios por qué no puedes acceder por índice a un set.
'''

print(estructura_lista[1])
print(estructura_diccionario['nombre'])
#El set no se puede acceder a los elementos porque los elementos no tienen indices ordenados asi que son objetos no estructurados.

'''
3. Contar e iterar
• Usa len() para mostrar la cantidad de elementos en cada estructura.
• Itera sobre cada estructura usando un for y muestra cada elemento por pantalla.
'''

print(len(estructura_lista))
print(len(estructura_tupla))
print(len(estructura_set))
print(len(estructura_diccionario))

for i in estructura_lista:
    print(i)
for i in estructura_tupla:
    print(i)
for i in estructura_set:
    print(i)
#Para los diccionarios debes traer el metodo .values para traer los valores y no las llaves del diccionario
for i in estructura_diccionario.values():
    print(i)

'''
4. Modificar estructuras
• Agrega un nuevo elemento a la lista y al conjunto.
• Borra un elemento de la lista.
• Agrega una nueva clave al diccionario.
• Intenta modificar la tupla y comenta qué ocurre.
'''

estructura_lista.append('lechuga')
estructura_lista.remove('pomelo')
print(estructura_lista)
estructura_diccionario['comuna'] = 'Maipu'
print(estructura_diccionario)
#estructura_tupla.append('mesa')
#No permite hacer modificaciones a la tupla porque es una lista inmutable, si quisiera agregar elementos deberia convertirlo en una lista para agregar elementos y
#regresar su estado de tupla

