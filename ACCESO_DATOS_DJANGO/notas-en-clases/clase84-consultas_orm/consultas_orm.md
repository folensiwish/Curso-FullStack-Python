Consulta uno a muchos:

Estamos trabajando con 2 models, y queremos consultar el modelo hijo a traves del padre.
En consultas SQL eso seria con un JOIN, ahora con el ORM se puede consultar mas sencillo, lo que se debe hacer es en el parametro del models hijo en el cual esta la relacion, 1 a muchos, muchos a muchos o 1 a 1, otorgarle el parametro de related_name = nombre-relacionado-hijo. Despues que tengamos eso y añadimos informacion a los modelos, consultamos con el siguiente codigo.
    instancia-padre.related_name.all() o get() o filter() etc..

Si lo llevamos a lo real tenemos 2 models, autor y libro. Entonces lo relacionamos con 1 a muchos. En la clase libro en el atributo relacion debemos pasarle esos parametros:
    autor = models.ForeignKey (Autor,on_delete=models.cascade, related_name=libros)
Para asi luego añadir infomacion a los models, crear la instancia autor, crear libros entregnadole la instancia autor.
Luego hacemos la consultas usando la instancia ejemplo
    autor1.libros.all() o get() o filter(), etc...

Ahora tambien podemos acceder la informacion de la entidad padre a traves del hijo, usando el nombre de la variable relacionada y el campo a traer de la entidad padre:
    ej : Libro.objects.filter(autor__nombre = 'Alberto')

Para usarlo en las vitas, debemos importar from .models import Libro

    creamos una instancia y le entregamos todo los datos ej:
        instancia-libro = Libro.objects.all()
    y lo pasamos por parametro al context={}, para luego en el template recorrer la instancia con un for y generar la logica que quieres implementa con las etiquetas a traves de jinga que son los {% %}

A considerar, no añadir informacion a los models desde las views porque cada vez que se visite ese endpoint el template ejecutara el codigo repetidas veces, Pero aca lo importante si queremos guardar informacion a la base de datos a traves de formularios en el template debemos en la view preguntar:
    if el request.method = post , ahi creamos el objeto usando la ORM ej: Objeto.objects.create(nombre = request.POST['nombre]) 