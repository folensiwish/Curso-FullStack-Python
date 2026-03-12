Implementacion:
    Controlar los acceso del sistema:
        -Se implemento el decorador login_required para restringir al usuario poder visualizar el home de la aplicacion sin logearse
    Se ocupo las tablas auth:
        -Colocando el path: path('accounts/',include('django.contrib.auth.urls')) para poder ocupar el login y logout en la bd
    Manejo de autoriazacion y permiso:
        En la views se importo permission_required para usar el decorador arriba de la funcion contenedora de la logica
    Redirrecionamiento de accesos no autorizados:
        Si un usuario intenta entrar a una ruta protegia lo redirije automaticamente al login eso para porque configuramos en settings.py 
    PermissionrequierdMixin:
        Lo configuramos a traves de la vista colocando el decorador encima de la funcion a proteger.