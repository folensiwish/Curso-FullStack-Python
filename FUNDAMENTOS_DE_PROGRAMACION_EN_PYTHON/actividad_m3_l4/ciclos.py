'''
1. Uso básico de while
Escribe un programa que imprima los números del 1 al 5 usando un ciclo while.
'''
#Inicializo una variable en 0 para ejecutar la condicion que se cumpla y luego ir sumando en 1 la variable para que luego imprima la secuencia hasta que la condicion no se cumpla.
numero = 0
while numero < 5:
    numero +=1
    print(numero)

'''
2. Uso básico de for
Escribe un ciclo for que recorra una lista de frutas (["manzana", "plátano", "naranja"]) y las imprima
en pantalla.
'''
#Se recorre la lista asignandolo en una variable i para luego imprimir la lista
lista_fruta = (['manzana','plátano','naranja'])

for i in lista_fruta:
    print(i)

'''
3. Condición en un ciclo
Crea un ciclo for que recorra los números del 1 al 10. Si encuentra un número par, imprime "Par", si es impar,
imprime "Impar".
'''
# Creamos un for con rango hasta el 11 para que nos tome el numero 10, luego hacemos la condicion de ver si el residuo que nos deja es 0 indica que es par y si es diferente a 0 es impar
for i in range(1,11):
    if i % 2 == 0:
        print(i, "Par")
    else:
        print(i, "Impar")

'''
4. Ciclo infinito controlado con break
Escribe un ciclo while True que solicite ingresar un número. El ciclo debe terminar si el número ingresado es
0. Usa break para salir.
'''
#Usamos la palabra para que funcione el ciclo hasta que si la condicion que el numero sea 0 se cumpla se salga del ciclo por la palabra reservada break
while True:
    numero = float(input("Ingrese un numero: "))
    if numero == 0:
        break

'''
5. Ciclo anidado
Escribe un programa que imprima una tabla de multiplicar del 1 al 3, usando un ciclo for dentro de otro for.
'''
#Generamos 2 for que recorren del 1 al 3 al entrar en el primer for la i toma el valor de 1 y al entrar al for j tambien toma el valor 1 y luego se hace la operacion de multiplicacion para luego imprimirlo con la variable resultado, asi hasta que se cumpla el ciclo for.
for i in range(1,4):
    for j in range(1,4):
        resultado = i*j
        print(i , "*" , j , "=" , resultado)

'''
6. Uso de continue
Recorre una lista de nombres. Si el nombre es "Juan", omítelo usando continue. Imprime todos los demás.
Recuerda aplicar snake_case para las variables y comentar cada ejercicio explicando qué hace el
ciclo y qué controla su finalización.
'''
#Se creo una lista con nombres para recorrer con la variable i, hacemos una condicion preguntando si i es igual a Juan este lo ignore y siga recorriendo e imprimiendo la lista.
lista_nombres = ['Juan','Alberto','Andres','Ashly']
for i in lista_nombres:
    if i == 'Juan':
        continue
    else:
        print(i)
