Consulta Mucho a muchos:
    Una cualidad nueva que se pueda agregar en los modelos es choice de django: lo que hace es entregarle una listado de tuplas con valores definidos para usar solo con esas opciones:
        ej: tamaño del producto
            SIZE_CHOICES = [('XL', 'grande')('M', 'mediano')('S', 'pequeño')]
    Una vez realizada la lista de tuplas, le otorgamos por parametro al atributo:
            choices=SIZE_CHOICES

Creamos la relacion ManyToManyField en el atributo referenciando la clase padre y queremos añadir informacion a la entidad hijo, no podemos pasarle la instancia a esa relacion. Porque son de muchos a muchos, que se hace entonces?
    Se añade informacion a los atributos sin referenciar el atributo relacionado ejemplo:
        Tengo la clase Salsa y los atributos:
            sandwich = models.ManyToManyField(Sandwich)
            nombre = nombre.CharField(max_length=20)
    Al crear la instancia lo hacemos con la siguiente sintaxys:
        salsa1= Salsa.objects.create(nombre='mayonesa')
    Como se puede apreciar no se hace uso de pasarle por parametro la instancia anterior creada con el sandiwch, solamente se añade los atributos que no tienen la relacion con la clase padre

    