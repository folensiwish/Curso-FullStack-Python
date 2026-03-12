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


Como validar el formulario: 

    Buena pregunta. Todo viene del objeto form que la view le pasa al template. Te explico cada uno:

    El objeto form
    En la view haces esto:
    pythonform = ContactoForm()
    return render(request, 'contacto.html', {'form': form})
    Eso le manda al template un objeto form de Django, y ese objeto tiene atributos útiles por cada campo.

    Los atributos de cada campo
    Cuando escribes form.nombre, accedes al campo "nombre" del formulario. Ese campo tiene:
    form.nombre.id_for_label
    → Django genera automáticamente un id HTML para el campo, generalmente id_nombre. Lo usas en el for= del label y en el id= del input para que estén vinculados.
    form.nombre.html_name
    → Es el name="" del input, o sea "nombre". Django lo usa para leer el valor cuando llega el POST.
    form.nombre.value
    → El valor actual del campo. Si el form tuvo errores y se re-renderiza, este valor contiene lo que el usuario ya escribió, para no perderlo. El |default:'' es por si viene None.
    form.nombre.errors
    → Una lista con los mensajes de error de ese campo. Si el campo está vacío o inválido, Django pone el mensaje aquí. Si no hay errores, la lista está vacía y el {% if %} no entra.

    De dónde vienen los errores
    Los errores los genera Django automáticamente cuando llamas form.is_valid() en la view. Django revisa las reglas del campo (si es requerido, si el email tiene formato válido, etc.) y llena form.campo.errors con los mensajes correspondientes.
    pythonif form.is_valid():   # ← aquí Django valida y llena los errores
        ...
    # si no es válido, el form ya tiene los errores adentro
    return render(request, 'contacto.html', {'form': form})  # ← se los mandas al template
    Entonces en el template simplemente los lees:
    html{% for error in form.nombre.errors %}
        {{ error }}   {# ← esto es el texto del error, ej: "Este campo es obligatorio" #}
    {% endfor %}
    ```

    ---

    ## Resumen visual
    ```
    ContactoForm  ←──── forms.py (tú defines los campos)
         │
         ▼
    form.is_valid()  ←── Django valida y llena los errores
         │
         ▼
    render(..., {'form': form})  ←── se manda al template
         │
         ▼
    template:
      form.nombre.id_for_label  →  "id_nombre"
      form.nombre.html_name     →  "nombre"
      form.nombre.value         →  lo que escribió el usuario
      form.nombre.errors        →  ["Este campo es obligatorio"]
    En resumen: Django hace todo el trabajo pesado, tú solo decides cómo mostrarlo en el HTML.
