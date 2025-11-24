'''
1. Decisión simple
Solicita al usuario ingresar un número. Si es mayor o igual a 18, imprime "Eres mayor de edad". Si no,
imprime "Eres menor de edad".
'''

numero = int(input("Ingrese su edad: "))

if numero > 0 and numero < 100:
    if numero == 18 or numero > 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

'''
2. Decisión múltiple con elif
Solicita al usuario una calificación (entre 1 y 7) e imprime el resultado evaluativo:
• 7 → Excelente
• 6 → Muy bien
• 5 → Bien
• 4 → Suficiente
• Menor que 4 → Insuficiente
'''

calificacion = int(input("Ingrese su calificacion de 1 a 7: "))

if calificacion == 7:
    print(calificacion , "--> Excelente")
elif calificacion ==6:
    print(calificacion , "--> Muy bien")
elif calificacion==5:
    print(calificacion , "--> Bien")
elif calificacion == 4:
    print(calificacion, "--> Insuficiente")
elif calificacion < 4:
    print(calificacion ,"Menor que 4 es --> Insuficiente")
   

'''
3. Condiciones anidadas
Solicita un número entero.
• Si es positivo, imprime "Número positivo".
• Si es cero, imprime "Es cero".
• Si es negativo, imprime "Número negativo".
Este ejercicio debe usar condiciones anidadas (if dentro de otro if).
'''

numero_entero = int(input("ingrese un numero: "))

if numero_entero == 0:
    print("Es cero")
else:
    if numero_entero > 0:
        print("Número positivo")
    else:
        print("Número negativo")

'''
4. Condición de borde
Solicita al usuario un número entre 1 y 100.
• Si el número es exactamente 1 o 100, imprime "Estás en un límite permitido".
• Si está dentro del rango pero no es extremo, imprime "Dentro del rango".
• En cualquier otro caso, imprime "Fuera del rango".
Asegúrate de usar nombres de variables en estilo snake_case y comentar el propósito de cada
bloque de código.
'''

# Asignamos una variable para que el usuario ingrese un numero.
entre_numero = int(input("Ingrese un número entre el 1 y 100: "))
#Se realiza una condicion donde evaluamos si el numero ingresado es igual a 1 o a 100.
if entre_numero == 1 or entre_numero == 100:
    print("Estás en un limite permitido")
#Se realiza una condicion donde se evalua que el numero ingresado se encuentra dentro del rango pero sacando de la ecuacion a los numeros extremos
elif entre_numero > 1 and entre_numero < 100:
    print("Dentro del rango")
#Si ninguna condicion cumple antes de llegar al else, se da por hecho que el numero ingresado puede estar fuera del rango.
else:
    print("Fuera del rango")

