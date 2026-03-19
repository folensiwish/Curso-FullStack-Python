
consultas_orm.py
Modelo preexistente
    class Libro(models.Model):
        titulo = models.CharField(max_length=100)
        autor = models.CharField(max_length=50)
        paginas = models.IntegerField()
        disponible = models.BooleanField(default=True)


Desarrolla los siguientes ejercicios utilizando el ORM desde el shell de Django o en una vista, y comenta
cada línea para explicar qué hace:
1. Recuperación de registros
• Recupera todos los libros registrados.
    instancia = Libro.objects.all() 

• Recupera solo los libros cuyo autor sea "Gabriel García Márquez".
    instancia = Libro.objects.filter(autor='Gabriel García Márquez') 

• Recupera los libros que tienen más de 200 páginas.
    instancia = Libro.objects.filter(paginas__gt=200) 

2. Filtros y exclusiones
• Aplica un filtro para mostrar solo libros disponibles.
    instancia = Libro.objects.filter(disponible=True)

• Excluye todos los libros que tengan menos de 100 páginas.
    instancia = Libro.objects.exclude(paginas__lt=100)
    
3. Consultas personalizadas con SQL
• Ejecuta una consulta SQL directa utilizando raw() para obtener todos los libros ordenados por titulo.
    instancia = Libro.objects.raw('select * from main_libro order by titulo asc')
• Usa connection.cursor() para ejecutar una query personalizada (por ejemplo, conteo de libros por autor)
y mostrar los resultados.
    cursor.execute("SELECT COUNT(*) FROM main_libro WHERE autor = 'Gabriel García Márquez'")  
        >>> resultado = cursor.fetchone()
        >>> print(f'El autor tiene {resultado} libros')
        El autor tiene (3,) libros
4. Campos específicos y anotaciones
• Recupera solo los títulos de todos los libros (usando values() o only()).
    >>> titulos_values = Libro.objects.values('titulo')
    >>> print(titulos_values)
        <QuerySet [{'titulo': 'Cien años de soledad'}, {'titulo': 'El amor en los tiempos del cólera'}, {'titulo': 'Crónica de una muerte anunciada'}, {'titulo': 'El Principito'}, {'titulo': 'Rayuela'}]>
    >>> titulos_only = Libro.objects.only('titulo')
    >>> print(titulos_only)
        <QuerySet [<Libro: Libro object (1)>, <Libro: Libro object (2)>, <Libro: Libro object (3)>, <Libro: Libro object (4)>, <Libro: Libro object (5)>]>
• Agrega una anotación (usando annotate) para contar cuántos libros hay por autor.
    >>> from django.db.models import Count
    >>> from main.models import Libro
        >>> conteo_por_autor = Libro.objects.values('autor').annotate(total_libros=Count('id')) 
        >>> for registro in conteo_por_autor:    
        ...     print(f"Autor: {registro['autor']} | Libros: {registro['total_libros']}")   
        ...    
        Autor: Gabriel García Márquez | Libros: 3  
        Autor: Julio Cortázar | Libros: 1 
        Autor: Antoine de Saint-Exupéry | Libros: 1


5. Reflexión (en un archivo aparte)
Crea un archivo resumen.md donde respondas:
• ¿Qué ventajas encuentras en usar el ORM frente a SQL tradicional?
    Lo mejor es que no tengo que salirme de python para poder escribir, considero que las consultas son mas cortas, ademas de lo fundamental de la seguridad y si me tengo que migrar a otra bd no tengo que tocar ninguna linea de mi consulta
• ¿En qué situaciones te parece útil ejecutar SQL directamente desde Django?
    Lo usaria para generar un reporte que sea super complejo con muchos join anidados o subconsultas porque en el orm se hace dificil leer, o si necesitaria hacer algo especifico donde la ORM no tiene mapeado, tambien si es que la consulta en django va lenta y necesito optimizarla.
• ¿Qué dificultades encontraste al trabajar con consultas más avanzadas?
    En el caso del raw no comprendia porque no me traia los campos en especifico que queria hasta que investigue y necesita pasarlo el id de la tabla para que funcione, me confundi con el cursor si bien entendi la logica de lo que hace al momento de escribirla y al tener tantos parametros tener cuidado con las comillas dobles y simples y el orden de agregar annotate con values o only porque te puede generar otro resultado que no esperabas.