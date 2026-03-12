¿Qué aprendiste sobre el flujo entre formulario, vista y template?
    La clave que aprender es que el form es el intermediario entre los tres. La view no le manda strings sueltos al template, le manda el objeto form entero, y el template sabe leerlo. Cada capa tiene su responsabilidad: el form valida, la view decide qué hacer, el template muestra.

¿Cuál es la ventaja de usar ModelForm?
    Las ventajas concretas son tres: no repites la definición de campos, las validaciones del modelo (como max_length) se aplican automáticamente al form, en vez de crear el objeto manualmente. 