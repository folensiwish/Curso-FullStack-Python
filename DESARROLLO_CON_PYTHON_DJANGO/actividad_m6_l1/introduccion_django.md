1. ¿Qué es Django?
    Django es un marco de trabajo, nos permite crear aplicaciones web y ayuda a realizar peticiones http conectando el front, backend y la base de datos entregandole al usuario una vista segun la logica del programa
• ¿Qué tipo de framework es Django?
    Django es un framework de alto nivel porque tiene todo lo necesario para construir una app web completa: manejo de base de datos, sistema de templates, autenticación, formularios.

• ¿Qué tipo de aplicaciones permite construir?
    Redes sociales, Tiendas online, Sistemas de gestion, blogs, Apis.

• Menciona al menos tres ventajas de usar Django sobre trabajar con Python puro para desarrollo web.
    Sistema de autenticacion, ORM que permite escribir codigo desde python para manejar la bd, admin panel automatico.

2. Entornos virtuales en Python

• ¿Qué es un entorno virtual en Python y para qué sirve?
    El entorno virtual permite tener dependencias independientes sobre los otros proyectos de python sin afectar los otros proyectos

• ¿Qué ventajas tiene crear un entorno virtual para un proyecto Django?
    Diferentes versiones de django segun el proyecto, evitar conflictos con dependencias de distintos proyectos, dar a conocer las versiones utilizadas en mi proyecto para que otros puedan usarlo o clonarlo.

• Explica en tus palabras qué hace el siguiente comando (no es necesario ejecutarlo):
    Este comando crea un entorno virtual, lo que hace es crear una carpeta con el nombre que le pusiste que contiene python y pip para instalar paquetes de forma aislada

3. Estructura y diseño de Django

• ¿Qué es el patrón MVC y cómo se aplica en Django (MTV)?
    MVC es un patrón de diseño que separa la aplicación en tres componentes: Model (datos), View (presentación) y Controller (lógica). Django usa MTV que es básicamente lo mismo pero con nombres diferentes
Completa esta tabla comparativa:
Concepto tradicional | (MVC) Nombre en Django (MTV) | Función
Model                | Model                        | Maneja los datos de la bd
View                 | Template                     |  Define lo que se le va a mostrar al usuario
Controller           | View                         | Representa la logica aplicada de la aplicacion o logica de negocio

• ¿Qué es el enrutador de Django y qué papel cumple en una aplicación web? 
    El enrutador o sistema de URLs de Django es el que mapea las direcciones web con las funciones que deben ejecutarse

4. Principios del desarrollo con Django
• ¿Qué significa el principio DRY ("Don't Repeat Yourself") y cómo lo aplica Django?
     significa no duplicar código. Si algo se repite, hay que convertirlo en una función o componente reutilizable. Django lo aplica dandote herramientas como template base
        
• ¿Qué significa que Django tenga una “estructura flexible y minimalista”?
    Significa que Django te da las herramientas necesarias pero no te obliga a usar todo. Puedes empezar simple (solo con modelos y vistas) e ir agregando complejidad según necesites. No tienes que configurar mil cosas para empezar, viene con configuraciones por defecto sensatas.

• ¿Qué son los Templates en Django y qué rol cumplen en la renderización de contenido?
    Los templates son archivos HTML con sintaxis especial de Django (usando {{ }} y {% %}) que nos permiten generar páginas dinámicas. Su rol es tomar los datos que les pasa la vista y renderizarlos en HTML que el navegador puede mostrar. Separan la presentación de la lógica del programa.