Agilidad en el desarrollo de aplicaciones:
    Desarrollar en django es muy sencillo, bueno, ademas trae componentes ya creados para usar y es bastante seguro, hace front, backend, devuelve respuestas http.

Es muy escalable, podemos pasar de poco a mucho en tiempo muy corto que sea estable y rapido.

Sus ventajas:
    ORM: permite hacer consultas SQL dentro del archivo python para conectarse a la bd.

Bibliotecas:
    csrf: seguridad
    flatpages: administrar contenido HTML simple
    markup: conjunto de filtros de plantillas de django, implemetan varios lenguajes de marcados conocidos.
    redirects: framework para administrar redirecciones
    sessions: framework de sesiones de Django
    HttpRequest: cuando se solicita una pagina, django crea un objeto HttpRequest que contiene metadatos sobre la solicitud

Enrutador de django:
    Diferentes puntos de accesos, sumamente sencillo, escalable permitiendo la modulizacion, el path significa los distintus puntos de accessos que tiene la aplicacion.

MVC: Vista controlador, el modelo el es el comun para la web.

django es MTV: modelo template view.

Modelo es donde se  interactua y comunica con la informacion alojado en la base de datos
Template es lo que vamos a mostrarle al usuario, es nuestra vista para el uso de HTML.
View vendira siendo lo que engloba la logica del negocio.

![alt text](image.png)

Descripcion de la imagen:
    El navegador va a consultar la URL map le va a consultar a la vista de django, tiene la opcion de mostrar directamente un template (login),
    Luego de ingresar las credenciales la peticion va a ir a la vista para luego ir al modelo para conectarse a la bd con las credenciales y ver si es verdadera las credenciales, le devuelvo el template del home, si no le entrega otro template o alerta de que las credenciales son incorrectas.

DRY: Dont repeat yourself;
    Modulizar el codigo para que el codigo sea reutilizable, 

La carpeta que crea el django-admin startproject nombredelaapp sirve para la configuracion del proyecto
comando para crear la aplicacion del proyecto: python manage.py startapp nombredelaapp

el archivo asgi.py, no se nota nunca, sirve con el tema de configuracion
el archivo urls.py va a tener el enturador del proyecto, va a tener todas los url.
el archivo settings.py este archivo tiene todas las configuraciones del proyecto, django importa Path desde pathlib, Las variables en mayusculas son variables que no se deben modificar, BASE_DIR, nos da la ruta del proyecto.
SECRET_KEY: la palabra que nos permite encriptar todo lo que tiene la aplicacion.
DEBUG = True , Nos permite ver los log de los errores
INSTALLED_APPS, agregar la app creada a la lista. ej usuarios
MIDDLEWARE, 
ROOT_URLCONF, sistema enrutado principal
TEMPLATES, donde va a estar el sistema de templates
WSGI_APLICATTION = 
DATABASES , 

VIEW.py desde la app usuarios, va a ser donde vamos a crear la logica de nuestra aplicacion
models.py donde vamos a hacer las tablas bd de nuestra aplicacion
admin.py, la cual le vamos a dar acceso a nuestro panel de administrador a la bd
 
Un proyecto de django esta creada por aplicaciones, cuando uno instala una aplicacion nueva debe colocarla en la lista INSTALLED_APPS en el settings.py

Actividad:
    Realizar actividad 1 del modulo 6