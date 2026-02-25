Independencia de rutas de la app con include a la URLS.py del proyecto:
Esto que significa y como se hace:
    1. Crearemos el archivo urls.py en la carpeta de la app
    2. Importaremos include con path cuando lo traemos desde django.urls
    3. Colocaremos en el urls.py del proyecto, path('url que queremos que sea vea en la web', include('nombredelapp.urls')), esto se debe hacer una vez. trae muchas ganancias por si la app crece.
    4. Configuraremos todas las urls en la app con views.nombredelafuncion como estuvo desde el inicio

Para cargar los archivos estaticos a la plantilla html, debemos usar la etiqueta:
    1. {% load static %} : Sirve para cargar los archivos a la plantilla
    2. Para cargar imagenes con la etiqueta : <img src="{% static 'img/imagen.jpg' %}"></img>, dentro del src de la imagen debemos poner la etiqueta para cargar la imagen que se desglosa asi: static es la carpeta contenedora y entre comillas simples colocamos la ruta en donde se encuentra el archivo.
    3. Para cargar js debemos generar le etiqueta scripts como se hace normalmente solamente que ahora debemos colocar la etiqueta static para dirigirnos al archivo js de la misma manera como encontramos la imagen entre comillas simples ej:
        <script src="{% static 'js/scripts.js' %}"></script>