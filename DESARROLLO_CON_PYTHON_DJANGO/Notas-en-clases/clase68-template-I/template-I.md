TEMPLATES:
    Permite al usuario tener la vista de la app para que pueda interactuar con ella.

En settings.py del proyecto, hay una lista llamada TEMPLATES y dentro de la lista aparece un DIRS, que es la direccion donde va a buscar la configuracion del proyecto los TEMPLATES. Cuando la lista DIRS esta vacio el proyecto entiende que cada aplicacion manejara la ubicacion de sus TEMPLATES por el contrario si es que en la lista DIRS le espicifico la ruta en donde va a buscar los TEMPLATES djando va a ir a esa ruta y buscara los TEMPLATES ahi.

Para implementar una plantilla TEMPLATE con la vista y la URL:
1. Se debe crear la url con un nombre asociativo a la pagina
2. Se debe crear la funcion retornando un render y pasandole por parametros request y lapagina.html
3. Debe crearse la carpeta TEMPLATE que contiene los templates de la app
4. Crear el archivo lapagina.html 
5. Generar codigo HTML para mostrar en la pagina

Para involucrar codigo dinamico, debemos en la funcion de la view segun la pagina.html escribir context pasandole la llave y el valor literalmente un diccionario. 
Para luego invocarlo en el archivo html a traves de -> {{}} y dentro de las llaves el hombre de la llave

Para aplicar codigo python en los archivos HTML, usaremos {% codigo python %} y para cerrar ese codigo {% endcodigopython %} y entre medio como queremos que se muestre ya sea una lista, parrafo, titulo, etc.
    por ejemplo: {% if condicion%} y {% else %} lo cerramos con {% endif %}
                {% for condicion %} y cerramos con {% endif %}

****DEJAR LA MAYOR LOGICA EN LA VIEW PORQUE EN LA PLANTILLA HACE QUE EL RENDER DEBA HACER MAS TRABAJO Y GENERAME MAS ESFUERZO DE LECTURA****

Actividad crear proyecto y app con 2 templates en la cual 1 template tendra contenido estatico y el otro dinamico.