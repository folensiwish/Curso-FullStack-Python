Usamos esto para redireccionar en una pagina que contiene detalles de algun item:
    Se usa para ver los detalles sobre el item en profundidad dirigiendose a este en un nuevo template, por ejemplo de productos para poder ver los detalles de los productos este nos va a direccionar a una pagina nueva, como lo hacemos?:

En la etiqueta <a> del template debemos:
    1. En el urls debemos tener configurado el name de la url para hacerlo llamar y redirrecionar a esa pagina
    2. debemos crear una variable en este caso nombre_movie y anteponer un signo de pregunta (?)
    3. Entregar el valor a la variable en este caso lo identifico por el nombre de la pelicula en otros casos puede ser por el id
        Aca esta el ejemplo con todo el detalle:
            <a href="{% url 'perfil'%}?nombre_movie={{nombre}}">detalles de la pelicula</a>
    
El metodo get, lo que haremos es obtener informacion de la variable creada en el href del template:
    1. Creamos una variable 
    2. Asignamos a la variable el metodo request.GET[]
    3. Le pasamos por parametro la variable creada en el href para direccionarnos a la pagina
        variable = request.GET['variable_del_template']
    Esto nos permitira traer un indice o nombre para la cual vamos a identificar el objeto que traeremos a la vista del usuario

    Vamos a instanciar la clase y por parametro le pasaremos la variable creada anteriormente, para asi traer informacion desde la instancia segun el indice pasado recientemente por la variable.
    1.Crear una variable
    2.Asignamos esa variable a la instancia de la clase para poder traer la informacion, puede ser una lista, diccionario, base de datos, etc..
        variable = DICCIONARIO_EJEMPLO['la_variable_del_request.GET']
    3.Usamos esta variable de la instancia para pasarla en context={} y poder utilizarla en el template según convengamos.

    Con esos pasos obtenemos la informacion que la almacenamos para luego usarla en el template con el context = {}, segun sea conveniente en el caso. ej Mostrar nombres,precio,productos,stocks,etc..

En el Template del detalle como mostramos la informacion:
    1. Creamos un for para poder recorrer las llaves y sus valores
    2. Retornamos los valores que queremos mostrar y las colocamos dentro de las etiquetas correspondientes
        Ejemplo:
            <h1>Detalle pelicula</h1>
                {% for columna,valor in indice.items %}
                    <li>{{columna}} - {{valor}}</li>
                {% endfor %}
             <a href="{% url 'home' %}">Volver atras</a>

En el template principal que luego redirige a estos detalles a traves de query-params:
    1. Recorremos el diccionario indicando el nombre del item en cuestion
    2. Le otorgamos el link para detalles del item y pueda ser redirigido segun la identificacion del item
        Ejemplo:
            <h1>Productos</h1>
            <ul>
                {% for nombre in cartelera.items %}
                    <h1>La pelicula es {{nombre}}</h1>
                    <a href="{% url 'perfil'%}?nombre_movie={{nombre}}">detalles de la pelicula</a>
                {% endfor %}
            </ul>

    