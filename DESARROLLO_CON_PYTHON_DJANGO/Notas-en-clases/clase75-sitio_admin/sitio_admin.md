Usar comandos previos para acceder al panel de administracion donde se aloja la base de datos:
    1.python manage.py makemigratios:
        sirve cuando creamos en el codigo una tabla y poder dejarla pre-migrada indicandole que esta listo para ser ejecutada
    2.python manage.py migrate:
        Hace los cambios permanente sobre las tablas en la bd,panel de administracion
    3.python manage.py createsuperuser:
        Sirve para crear al usuario admin que tiene permisos de todo en la app
    4.python manage.py runserver:
        Para correr el servidor

Por detras podemos identificar el acceso al panel de administracion con el user.is_staff == True para otorgarle el permiso de acceso al panel de control

django rest framework para generar api mas sencillas quizas automatizadas?

clase 77 y clase 78 para revisar y poder hacerlo en tiempo libre.