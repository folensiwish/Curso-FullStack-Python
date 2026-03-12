Login y logout esta preterminada y automatizada, hace todo por debajo sin la necesidad de nosotros crear algo. Como lo hace con django-auth.

Dentro de django tenemos la representacion de la bd en los models, como nos trae automaticamente, nos automatiza la tabla de usuarios como tambien el login y logout, tiene atributos ciertamente limitados. 

Las contraseñas quedan encriptadas con hash seguro, por lo tanto debemos tener cuidado con la api key de django.
Puede proteger vistas, segun el usuario se puede dar acceso a ciertos endpoints. Si es que el usuario no esta registrado le va a bloquear el paso a las paginas lo mandara a iniciar sesion.

De las 2 vistas que proporciona django con el tema del login en el settings.py

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

asi puedes controlar de donde va a dirigirse el usuario automaticamente

Como activar el authentication predeterminada de django en las urlpatterns del proyecto en urls.py
    urlpatterns = [
        path('accounts/', include('django.contrib.auth.urls'))
    ]
eso activa los endpoints predeterminados por django:
    ![alt text](image.png)

Por definido el proyecto va a buscar la carpeta templates/registration que debe contener obligatoriamente el nombre de login.html

Para activar el acceso a los endpoints de la app por parte de los usuarios debemos importar el login required que nos indica que solo tendran acceso las personas que hicieron login en la aplicacion:
    entonces en el views de la app importamos el siguieente elemento:
        from django.contrib.auth.decorators import login_required

    Ademas debemos hacer una funcion e invocar (decorar) el login required con lo siguiente:
        @login_required
        
        def bienvenido(request):
        private_flans = Flan.objects.filter(is_private=True)
        return render(request, 'welcome.html', context = {'private_flans':private_flans})

Paso a paso:
    Antes de todo debemos migrar y crear el superusuario con los siguientes comandos:
        python manage.py migrate
        python manage.py createsuperuser

    1. Creamos la carpeta registration/login.html
    2.Creamos el formulario dentro del login.html, donde iran los label y los campos input con el botton de submit. Lo importante es esto:
        Que contenga en el form el action 'login' y el method sea post <form action="{% url 'login' %}" method="post">
        Ademas dentro de las etiquetas input debe ir apodado segun el campo -> name='username' o name='password' en este caso deben ser asi para que el sistema de django los tome automaticamente.
    3. Escribimos el token -> {% csrf_token %}

    4.Teniendo el index.html que seria la pagina principal debemos colocar una url para ir al login:
        <a href="{% url 'login' %}" class="btn btn-primary">Login</a>

    5.Para hacer el log out sea cual sea el template en el cual queremos colocar el boton para cerrar sesion colocaremos el siguiente codigo:
        Esta es la base que debe tener si o si:
            <form action="{% url 'logout' %}" method="post">
                {% csrf_token %}
                <button type="submit" class="btn btn-danger">Log Out</button>
            </form>
    6. Para que los endpoints de django auth funcionen debemos colocar en settings.py del proyecto:
        LOGIN_REDIRECT_URL = 'perfil' #Donde quiero que entre luego de ingresar las credenciales correctamente
        LOGOUT_REDIRECT_URL = 'login' #Donde quiero que me redireccione luego de cerrar sesion

    7. Para proteger las rutas de los endpoints de los usuarios que no se han logeado debo hacer lo siguiente:
        7.1 Ir a views e importar:
            from django.contrib.auth.decorators import login_required
        7.2 Escribir por encima de la funcion del endpoint a proteger lo siguiente:
            @login_required
    8. django tiene una instancia user, que nos permite acceder a toda la informacion y mostrarla al usuario si es conveniente, colocando en el template {{user.username}} o {{user.first_name}} o {{user.last_name}} según este modelado en la base de datos.

Actividad hacer lo mismo, para reforzar los conocimientos.