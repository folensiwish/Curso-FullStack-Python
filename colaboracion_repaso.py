'''
🟢 NIVEL BÁSICO
🟢 Ejercicio 1: Persona – Dirección
Objetivo: entender objeto dentro de objeto
Enunciado

Crea las clases:

Dirección
atributos: calle, numero
método: mostrar()

Persona
atributos: nombre, direccion (instancia de Dirección)
método: mostrar_info()

Reglas
La Dirección se crea fuera y se pasa a Persona.
Persona debe usar el método de Dirección.
'''
'''
class Direccion:

    def __init__(self,calle,numero):
        self.calle = calle 
        self.numero = numero
    
    def mostrar(self):
        print(f'La calle se llama {self.calle} y el numero {self.numero}')

class Persona:

    def __init__(self,nombre,direccion):
        self.nombre = nombre
        self.direccion = direccion
    
    def mostrar_info(self):
        print(f'El nombre de la persona es {self.nombre}')
        self.direccion.mostrar()

dir1 = Direccion('San jose','1726')
p1= Persona('Alberto',dir1)
p1.mostrar_info()

'''

'''
🟢 Ejercicio 2: Libro – Autor
Objetivo: usar atributos de otra clase
Enunciado

Clases:
Autor
atributos: nombre
método: mostrar()

Libro
atributos: titulo, autor (instancia de Autor)
método: mostrar_info()
'''
'''
class Autor:

    def __init__(self,nombre):
        self.nombre = nombre
    
    def mostrar(self):
        print(f'El nombre del autor es {self.nombre}')
    
class Libro:

    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
    
    def mostrar_info(self):
        print(f'El titulo del libro es {self.titulo}')
        self.autor.mostrar()

a1 = Autor('Alberto')
l1= Libro('Principito',a1)
l1.mostrar_info()
'''

'''
🟡 NIVEL BÁSICO + LISTAS
🟡 Ejercicio 3: Curso – Estudiante
Objetivo: lista de objetos
Enunciado

Clases:
Estudiante
atributos: nombre
método: mostrar()

Curso
atributos: nombre, estudiantes (lista de Estudiante)
métodos:
agregar_estudiante(estudiante)
mostrar_estudiantes()
'''
'''
class Estudiante:

    def __init__(self,nombre):
        self.nombre = nombre
    
    def mostrar(self):
        return self.nombre

class Curso:

    def __init__(self,nombre):
        self.nombre = nombre
        self.estudiantes = []
    
    def agregar_estudiantes(self,estudiante):
        self.estudiantes.append(estudiante)
    
    def mostrar_estudiantes(self):
        print(f'El nombre del curso es {self.nombre}.')
        print('Los alumnos inscritos son: ')
        for i in self.estudiantes:
            
            print(i.mostrar())



e1=Estudiante('Alberto')
e2=Estudiante('Ashly')
e3=Estudiante('Roberto')
c1=Curso('Taller Ingles')
c1.agregar_estudiantes(e1)
c1.agregar_estudiantes(e2)
c1.agregar_estudiantes(e3)
c1.mostrar_estudiantes()
'''

'''
🟡 Ejercicio 4: Carrito – Producto

Objetivo: acceder a atributos dentro de lista
Enunciado

Clases:
Producto
atributos: nombre, precio

Carrito
atributos: productos (lista de Producto)
métodos:
agregar_producto(producto)
calcular_total()
'''
'''
class Producto:

    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:

    def __init__(self):
        self.productos = []
    
    def agregar_producto(self,producto):
        self.productos.append(producto)
    
    def calcular_total(self):
        total = 0
        for i in self.productos:
            total += i.precio
        return total

    def mostrar_carrito(self):
        print('\nCarrito de compras')
        print('-'*30)
        for i in self.productos:
            print(f'El producto {i.nombre} su precio es ${i.precio}')
        print(f'El total a pagar es de: ${self.calcular_total()}')



p1=Producto('Libreta', 5000)
p2=Producto('Notebook', 125000)
c1=Carrito()
c1.agregar_producto(p1)
c1.agregar_producto(p2)
c1.mostrar_carrito()
'''

'''
🟠 NIVEL INTERMEDIO
🟠 Ejercicio 5: Empresa – Empleado

Objetivo: cálculos usando datos de otra clase
Enunciado

Clases:
Empleado
atributos: nombre, sueldo

Empresa
atributos: nombre, empleados (lista de Empleado)
métodos:
agregar_empleado(empleado)
calcular_nomina() → suma sueldos
'''
'''
class Empleado:

    def __init__(self,nombre,sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    
class Empresa:

    def __init__(self,nombre):
        self.nombre = nombre
        self.empleados = []
    
    def agregar_empleado(self,empleado):
        self.empleados.append(empleado)
    
    def calcular_nomina(self):
        nomina = 0
        count = 0
        for i in self.empleados:
            nomina += i.sueldo
            count += 1
        print(f'El calculo de la nomina de la empresa {self.nombre } con {count} trabajadores es de ${nomina} pesos')
        
e1= Empleado('Alberto', 700000)
e2=Empleado('Ashly', 850000)
em1= Empresa('AFP plan vital')
em1.agregar_empleado(e1)
em1.agregar_empleado(e2)
em1.calcular_nomina()
'''

'''
🟠 Ejercicio 6: Factura – Item

Objetivo: cálculo con múltiples atributos
Enunciado

Clases:
Item
atributos: descripcion, precio, cantidad

Factura
atributos: items (lista de Item)
métodos:
agregar_item(item)
calcular_total()
'''
'''
class Item:

    def __init__(self,descripcion,precio,cantidad):
        self.descripcion = descripcion
        self.precio = precio 
        self.cantidad = cantidad

class Factura:

    def __init__(self):
        self.items = []
    
    def agregar_item(self,item):
        self.items.append(item)
    
    def calcular_total(self):
        total = 0
        for i in self.items:
            total += i.precio * i.cantidad
            print(f'El producto {i.descripcion} cuesta ${i.precio}')
        print(f'El total de la factura es: ${total}')


i1= Item('Caucho',45000,4)
i2= Item('Tela',10000,10)
f1= Factura()
f1.agregar_item(i1)
f1.agregar_item(i2)
f1.calcular_total()
'''

'''
🔵 NIVEL INTERMEDIO REAL (EXAMEN)
🔵 Ejercicio 7: Biblioteca – Libro – Autor

Objetivo: colaboración múltiple
Enunciado
Clases:
Autor
atributos: nombre

Libro
atributos: titulo, autor (Autor)

Biblioteca
atributos: libros (lista de Libro)
métodos:
agregar_libro(libro)
mostrar_catalogo()
'''
'''
class Autor:

    def __init__(self,nombre):
        self.nombre = nombre

class Libro:

    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor #Instanciar con el objeto Autor
    
class Biblioteca:

    def __init__(self):
        self.libros = []

    def agregar_libro(self,libro):
        self.libros.append(libro)
    
    def mostrar_catalogo(self):
        for i in self.libros:
            print(f'El titulo del libro es {i.titulo} y su autora {i.autor.nombre}')

au1= Autor('Ashly')
li1= Libro('Alas de sangre', au1)
bi1= Biblioteca()
bi1.agregar_libro(li1)
bi1.mostrar_catalogo()
'''

'''
🔵 Ejercicio 8: Pedido – Producto – Cliente

(El que ya estás dominando 💪)
Enunciado

Clases:
Producto (nombre, precio)

Cliente (nombre)

Pedido (cliente, productos)
calcular_total()
mostrar_resumen()
'''

class Producto:

    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio
    
class Cliente:

    def __init__(self,nombre):
        self.nombre = nombre

class Pedido:

    def __init__(self,cliente,producto):
        self.cliente = cliente #instanciar con el objeto Cliente
        self.producto = producto #instanciar con el objeto Producto
    
    def calcular_total(self):
        total= 0
        total += self.producto.precio
        return total

    def mostrar_resumen(self):
        print(f'El producto {self.producto.nombre} fue pedido por el cliente {self.cliente.nombre} y el total a pagar es de ${self.calcular_total()}')

pr1= Producto('Vaso', 3500)
pr2=Producto('Ventilador', 50000)
cli1= Cliente('Alberto')
cli2=Cliente('Ashly')
pe1= Pedido(cli1,pr1)
pe2=Pedido(cli2,pr2)
pe1.mostrar_resumen()

    