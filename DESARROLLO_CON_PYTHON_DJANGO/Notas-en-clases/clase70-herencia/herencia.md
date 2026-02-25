Herencia de templates: 
    Permite no lidiar con archivos con grandes cantidades de lineas, lo que se propone con tener un archivo base.html tener las importaciones, scripts, cdn, boostrap, etc.
Para reenderizar y que el motor de ejecucion jinja2 sepa cuando ejecutar el archivo y cuando terminar de ejecutarlo es escribe el siguiente codigo:
    {% block content %} y para cerrarlo {% endblock %}
Ademas, ponemos incluir secciones de la pagina que se puedan volver repititivas en las demas paginas, como el footer o el navbar asi no tenemos que copiar y pegar el footer y el navbar o cualquier otro elemento repititivo en todos los archivos html, y lo hacemos de la siguiente manera:
    {% block 'navbar' %} o {% block 'footer'%} o {% block 'repititivo' %}
    {% include 'navbar.html'%} o {% include 'footer.html'%}, etc..
    cerrando el bloque con {% end block %}
La base.html, es nuestro archivo padre donde todos los archivos se van a extender desde ahi por lo tanto se deben incluir las partes al archivo base.html

Para entender mejor esto, cada pagina va a tener su ruta establecida, menos la base html y secciones que esten incluidas en base.html. La idea principal es que la base html funcione como plantilla para las paginas que se van a mostrar al usuario y centrarse en el body para crear el contenido explicito para cada pagina.
Para que el renderizado tome en cuenta, debe extender la base.html con este siguiente comando en la primera linea:
    {% extends 'base.html %}
Si es que tiene archivos o scripts que se quieren adjuntar y se quiere solamente colocar en una pagina debemos cargar en la pagina en cuestion el 
    {% load static %}
Ademas el contenido del html debe ir envuelto en {% block content %} y {% endblock %} para que sea considerado en el renderizado y lo lea para mostrarselo al usuario.

Ademas hay una funcion nueva en las etiquetas <a> que permite redireccionar a otra pagina, con lo siguiente:
    Debemos ir a la urls.py de la aplicacion y agregar un nuevo parametro luego de indicar la vista con su funcion agregamos la coma para separar el parametro y colocamos:
        name = 'home' : Si es que el path se llama home, la idea es colocar el mismo nombre para saber de que trata
    Luego iremos a la etiqueta donde tenemos el link y agregamos:
        href= "{% url 'home' %}"
