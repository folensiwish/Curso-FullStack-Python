Crear super usuario con el comando: python manage.py createsuperuser

******La vista es un funcion que recibe una request y retorna un valor***********

En la consola nos aparecera este mensaje You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

Para poder acceder al panel de administrador y corregir esas 18 migrationes debemos usar el siguiente comando: python manage.py migrate
Una vez logeado puedes agregar usuarios manualmente, otorgandole permisos, asignandole contraseña para que pueda logear, agregar informacion personal sobre el usuario staff, borrar el usuario staff.

