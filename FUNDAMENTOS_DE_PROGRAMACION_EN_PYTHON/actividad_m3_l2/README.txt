a = [5,1,4,9,0]
b = range(3,10) + range(20,23)
c = [[1,2],[3,4,5],[6,7]]
d = ['perro','gato','jirafa','elefante']
e = ['a',a,2*a]

1. a[2] = 4 - Correcto
2. b[9] = error range diferente a listas - Correcto en error pero mas especificamente que el operador de suma no funciona sumando ranges
3. c[1][2] = 5 - Correcto
4. e[0] == e[1] = error syntaxis? - Incorrecto, Esta haciendo una comparacion por lo tanto debes corroborar si es True o False
5. len(c) = 3 - Correcto
6. len(c[0]) = 2 - Correcto
7. len(e) = error syntaxis por que la a no tiene comillas - Incorrecto, el resultado es 3 toma en cuenta los elementos que se encuentran en la lista y los cuenta. por lo tanto mi deduccion de porque la a no tenia '' es erroneo
8. c[-1] = 2 - Incorrecto, el [-1] indica el ultimo elemento de la lista y este al ser un grupo de numeros el resultado deberia ser [6,7]
9. c[-1][+1] = 6 - Incorrecto, el numero resultado de la operacion resulta ser 7
10. c[2:]+ d[2:] = error al realizar una operacion de numeros con string - Incorrecto, la operacion no intenta hacer una suma con numeros y letras lo que hace es una concatenacion de los elementos encontrados desde la posicion que se antepone de los : hacia delante.
11. a[3:10] = [5,1,4,10,0] - Incorrecto, al iniciar con 3 se toma la posicion de donde empieza hasta el 10 que es el numero que determina hasta donde termina la secuencia, en este caso como hay menos de 10 elementos el conteo se termina con el ultimo elemento de la lista
12. a[3:10:2] = [5,1,10,4,0] - Incorrecto, se inicia desde la posicion 3 que tiene el valor 9 y el largo de esta secuencia te indica que debe recorrer 10 elementos maximos de 2 en 2 por el numero final de la operacion pero al momento de tener solo 4 elementos en la lista en total al querer saltar del 3 al 5 se termina porque no hay mas por lo tanto el resultado final es el 9 porque es el ultimo elemento que cumplia con la condicion dada.
13. d.index('jirafa') = ['jirafa','perro','gato','elefante'] - Incorrecto, la funcion index() al pasarle un parametro te indica en que posicion de la lista este se encuentra.
14. e[c[0][1]].count(5) = error porque count no debe llevar parametros? es una funcion que te cuenta por lo tanto debe ir vacio el valor entre parentesis - Incorrecto, count si puede llevar parametros y te indica las veces que se repite el numero dentro de la lista. en este caso el 5 se repetia 2 veces por la operacion que se tenia que realizara para llegar al resultado final 
15. sorted(a)[2] = [4,5,1,10,0] , Correcto a medias, se sabia que el sorted ordena la lista y por el parametro 2 sabiamos que el 4 era el elegido ahora lo que no estuvo correcto fue incluir la demas lista y no solo dejar el 4 como el unico resultado
16. complex(b[0],b[1]) = error por que son rangos por lo tanto la syntaxis de las [] estan orientadas a las listas por lo tanto no se cumple la syntaxis del lenguaje y no se pueden sumar entre ranges , la solucion para poder sumar entre range es agregar la funcion list(range) para asi poder sumarlos