'''
1. Imprimir un mensaje inicial
Muestra en pantalla el texto:
"¡Hola! Este es mi primer programa en Python."
'''
print("¡Hola! Este es mi primer programa en Python.")

'''
2. Declarar variables simples
Declara las siguientes variables y muestra su contenido con print():
• Tu nombre
• Tu edad
• Tu ciudad
'''

nombre = "Alberto Fernandez"
edad = 28
ciudad = "Santiago"
print(nombre , edad , ciudad)

'''
3. Realizar operaciones básicas
Suma dos números y muestra el resultado. Usa comentarios para explicar cada línea.
'''
#Se le asigna a la variable num_1 un valor de 2
num_1 = 2
#Se le asigna a la variable num_2 un valor de 4
num_2 = 4
#Se imprime el resultado de la operacion
print(num_1 + num_2)

'''
4. Explorar un módulo integrado
Importa el módulo math y utiliza la función sqrt() para calcular la raíz cuadrada de un número.
(Ejemplo: math.sqrt(25) → debe mostrar 5.0)
Agrega comentarios explicativos en tu código para demostrar que comprendes cada instrucción.
'''
# Se llama a el modulo math a trabjes de import, porque python ya viene integrado con ese modulo sin necesidad de descargar nada
import math
#Luego se hace el llamado del modulo al escribirlo con la funcion incorporada de raiz cuadrada colocando en el entre parentesis
#El numero que deseamos obtener su raiz 
print(math.sqrt(5))