Que aprendi de la clase formulario:
    Una vez generado el proyecto y la aplicacion, creamos la ruta y la view con su template.
    En el template, creamos el formulario con el:
        method == 'POST'
    principalmente usaremos la plantilla prefabricada de bootstrap.
    Una vez hecho el formulario, pondremos la etiqueta:
        {% csrf_token %} : Sirve para la seguridad de django genera un token del envio del formulario
    Luego nos dirigimos hacia la view y hacemos una condicion:
        if request.method == 'POST'
            return render (request, 'plantilla.html', context={})
    Agregamos la logica dentro de la condicion, segun lo que necesitamos, ej:
        Recibir del formulario, los campos nombres,email,edad,contraseña y podemos generar un objeto persona para usarlo como prefriramos, o usar variables, para usarlas dentro de la plantilla o logica de la aplicacion
    Al final de la views dentro de la funcion cerramos con un:
        else
            return render (request, 'plantilla.html', context={})
    Aca lo que hacemos es darle una respuesta al usuario a su peticion, si es que no se cumplio con lo requerido del formulario se le entrega un mensaje de alerta que debe completar el formulario para enviar la peticion o solo se queda en la pagina esperando alguna solicitud del usuario.

    Al final del proceso del formulario, podemos en la plantilla generar la logica con python sobre listas,diccionarios,obtener id,imagenes,etc..
    como tambien mostrar un mensaje a traves de el tipado de jinja2 que serian con los -> {} y la variable dentro.
    