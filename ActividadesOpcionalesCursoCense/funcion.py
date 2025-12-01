'''
Crear una funcion que devuelva el mensaje "HOLA MUNDO 2"     cuando se invoque
'''
'''
def saludo():
    print("HOLA MUNDO 2")

saludo()
'''
'''
Crear una funcion que reciba como parametros 2 numeros y retorne la suma de estos como resultado con *args
'''
'''
lista = [1,2,3,4,5]
def suma(*args):
    value = 0
    for n in args:
        value +=n
    return value
#se debe colocar *antes de la variable como argumento porque asi el args puede interpretar los numeros 1 por 1 si no tomaria solo un elemento que sera la lista como lista y no se puede.
print(suma(*lista))
'''
'''
Crear una funcion que reciba 2 parametros, su nombre y apellido y retorne los parametros enviados a la funcion concatenados al mensaje "Bienvenido" **kwargs
'''
'''
nombre = input("Ingrese su primer nombre: ")
apellido = input("Ingrese su primer apellido: ")

dic = {    
    'nombre': nombre,
    'apellido': apellido,
}

def mensaje(**kwargs):
    print(f'Bienvenido {kwargs['nombre']} {kwargs['apellido']}')
mensaje(**dic)
'''


numero = int(input("Ingrese un numero: "))

for i in range(numero):
    print("*"*(numero-1))

