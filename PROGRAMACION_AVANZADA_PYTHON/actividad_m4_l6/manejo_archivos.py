'''
Instrucciones
Crea una carpeta llamada actividad_m4_l6 y dentro de ella, un archivo Python llamado
manejo_archivos.py. Este script debe resolver los siguientes ejercicios:

1. Escribir en un archivo
• Crea un archivo llamado datos.txt desde Python (modo escritura).
• Escribe al menos 3 líneas de texto en él usando write().
2. Leer el archivo completo
• Abre el archivo datos.txt en modo lectura y muestra su contenido en pantalla usando read().
3. Leer línea por línea
• Usa readline() para leer e imprimir solo la primera línea del archivo.
• Luego, usa un ciclo for para leer línea por línea el resto del archivo.
4. Añadir contenido (modo append)
• Vuelve a abrir el archivo en modo append y agrega una línea nueva.
• Luego vuelve a abrirlo en modo lectura para comprobar que se agregó correctamente.
5. Atributos y cierre
• Muestra por pantalla el nombre del archivo (.name), si está cerrado (.closed) y el modo de apertura
(.mode).
• Asegúrate de cerrar el archivo correctamente con .close() o usando with.
'''
#1 Escritura 
text = open('datos.txt', 'w') 

for i in range(3):
    text.write(f'Este es el {i} mensaje\n')

print(text.name)
text.close()

#2 y 3 Se lee el archivo solamente si esta cerrado.

with open('datos.txt', 'r') as leer:
    print(leer.read())

with open('datos.txt', 'r') as archivo:
    print(archivo.readline())
    for i in archivo:
        print(i, end='')

#4 modo append

with open('datos.txt', 'a') as agregar:
    agregar.write(f'Esta es una nueva linea')

with open('datos.txt', 'r') as leer:
    print(leer.read())

#5 

with open('datos.txt', 'r') as cierre:
    print(cierre.closed)
    print(cierre.name)
    print(cierre.mode)

print(cierre.closed)