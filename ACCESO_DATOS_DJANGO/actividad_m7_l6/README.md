• ¿Cómo funciona el flujo completo de una operación CRUD?
    Create : El usuario entra a /libros/crear/. El servidor entrega un formulario de Bootstrap vacío. Al llenar los datos y presionar "Guardar", la vista captura la información con request.POST, crea una instancia del modelo Libro y la guarda en la base de datos con usando Libro.objects.create().

    Read: Es la operación más común. La vista usa Libro.objects.all() para traer todos los registros. Estos se pasan a través de un diccionario de contexto al template listar_libros.html, donde se recorren con un ciclo {% for %} para armar la tabla.

    Update: Aquí combinamos búsqueda y edición. Primero buscamos el libro por su ID dinámico. Si el usuario envía cambios, usamos .filter(id=id).update() para refrescar los datos en la DB sin tener que crear un objeto nuevo.

    Delete: Implementamos un flujo seguro. Primero una página de confirmación para evitar accidentes, y luego la ejecución del borrado con .delete() tras la validación del usuario.

• ¿Qué aprendiste sobre el enrutamiento y los parámetros dinámicos en URLs?

    ¿Qué aprendí?: Que el valor que va en la URL (como el número 5) viaja como un argumento directo hacia la función en views.py. Esto permite que una sola vista pueda manejar miles de libros distintos simplemente recibiendo su "ID".
    Aprendí a usar el atributo name en las URLs. Esto es genial porque si después decido cambiar la ruta de /libros/ a /biblioteca/, no tengo que ir template por template cambiando los enlaces; Django lo actualiza solo gracias a la etiqueta {% url %}.