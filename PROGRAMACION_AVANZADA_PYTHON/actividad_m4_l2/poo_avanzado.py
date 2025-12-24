'''
1. Definición de una clase con constructor
• Crea una clase Libro con los atributos titulo, autor y anio_publicacion.
• Define un método constructor __init__() que inicialice esos atributos.
• Crea un método mostrar_info() que imprima los datos del libro.
'''
'''
2. Métodos accesadores y mutadores
• Implementa métodos get_titulo() y set_titulo(nuevo_titulo) para acceder y modificar el
atributo titulo.
• Repite lo mismo para el atributo anio_publicacion.
• Usa estos métodos para modificar el título de un libro desde el programa principal.
'''
'''
3. Sobrecarga de métodos
• En la clase Libro, crea un método resumen() que:
• Si no recibe parámetros, imprime "Libro sin resumen disponible".
• Si recibe un texto como parámetro, imprime ese resumen.
• Simula la sobrecarga usando valores por defecto y condicionales en el método.
'''
'''
4. Colaboración entre objetos
• Crea una clase Autor con atributos nombre y pais.
• Modifica la clase Libro para que el atributo autor sea un objeto de tipo Autor.
• En el método mostrar_info(), muestra también el nombre y país del autor.

'''
'''
5. Composición
• Crea una clase Editorial con atributos nombre y ciudad.
• Modifica la clase Libro para que tenga un atributo editorial (objeto de tipo Editorial).
• Asegúrate de que la instancia de Editorial se cree dentro del constructor de Libro.
'''

class Libro:

    def __init__(self,titulo,autor,anio_publicacion,nombre,ciudad):
        self.titulo = titulo
        self.autor = autor 
        self.anio_publicacion = anio_publicacion
        self.editorial = Editorial(nombre,ciudad)
    
    def mostrar_info(self):
        print(f'El libro tiene como titulo {self.titulo}, el autor se llama {self.autor.nombre} y el anio de publicacion del libro fue el {self.anio_publicacion}. El autor nacio en {self.autor.pais} en la ciudad de {self.editorial.ciudad}')

    def get_titulo(self):
        print(self.titulo) 
    
    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def get_anio_publicacion(self):
        print(self.anio_publicacion) 
    
    def set_anio_publicacion(self, nuevo_anio):
        self.anio_publicacion = nuevo_anio
   
    def mostrar_info_actualizada(self):
        print(f'Info actualizada: El libro tiene como titulo {self.titulo}, el autor se llama {self.autor.nombre} y el anio de publicacion del libro fue el {self.anio_publicacion}. El autor nacio en {self.autor.pais} en la ciudad de {self.editorial.ciudad}')

    def resumen(self,resumido=None):
        if resumido==None:
            print("Libro sin resumen disponible")
        else:
            print(resumido)

class Autor:

    def __init__(self,nombre,pais):
        self.nombre = nombre
        self.pais = pais

class Editorial:

    def __init__(self,nombre,ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

au1= Autor('Ashly', 'Chile')   
li1= Libro('Alas de sangre', au1 , 2019, 'Castellano','Santiago')
li1.mostrar_info()
li1.set_titulo('Alas de onix')
li1.set_anio_publicacion(2023)
li1.mostrar_info_actualizada()
li1.resumen()

