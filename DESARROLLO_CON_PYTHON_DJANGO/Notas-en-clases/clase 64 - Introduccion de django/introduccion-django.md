Que es django?
    Es un marco de trabajo (framework), que nos facilita el desarrollo en autenticacion,formularios,etc.. 

Que nos permite hacer django? 
    Principalmente es para responder a solicitudes https como tambien usarlos en otros puertos.

El entorno de desarrollo, permite desarrollar para no interrumpir la app de produccion, para no cometeres errores y botar la aplicacion, clonando el ambiente de produccion.

Ambiente de produccion, Esta listo la app para que el usuario este interactuando con la aplicacion.

Django soporta cuatro basese de datos relacionales, PostreSQL, MySQL, Oracle y SQLite.

El entorno virtual, Permite independizar del desarrollo el proyecto de otros, usando componentes, librerias y versiones unicas para ese proyecto. Como tambien permite no afectar los demas proyectos que se estan desarrollando.

¿Como crear entorno virtual?
    comando: python -m venv env  
Donde env es el nombre la cual quiero nombrar a mi entorno virtual.

¿Como iniciamos el entorno virtual?
    comando: env\Scripts\Activate, Para windows.

Actividad: 
    1. Abrir terminar
    2. Crear carpeta
    3. Crear entorno virtual
    4. Activar entorno virtual
    5. Instalar django
    6.Crear el proyecto con django-admin startproject nombredelproyecto
    7. Correr el servidor django
Objetivo: Mostrar el cohete que aperece en la pagina web
Usar gitbash para la consola en vez del cmd.

Apuntes del paso a paso del programa:
    Abrir la terminal bash
    Crear la carpeta con mkdir nombrecarpeta
    Crear entorno virtual con el comando python -m venv env 
    Activar el entorno virtual con el comando source env/Scripts/activate
    Crear el proyecto django-admin startproject nombredelproyecto
    Ingresar a la carpeta del proyecto nombredelproyecto
    Iniciar el servidor de django python manage.py runserver
