Sistema Educacional POO
Este proyecto es una implementación práctica de Programación Orientada a Objetos (POO) en Python. Simula la gestión académica de una institución, permitiendo interactuar con alumnos, profesores, asignaturas y carreras.

Guía de Inicio Rápido

Instalación: Descarga todos los archivos .py en una sola carpeta.

Ejecución: Abre tu terminal en esa carpeta y ejecuta:

python main.py

Estructura del Proyecto
El código sigue fielmente el Diagrama de Clases diseñado para el sistema:

persona.py: Clase base con datos comunes (RUT, nombre, email).

alumno.py: Hereda de Persona; gestiona matrículas y promedios.

profesor.py: Hereda de Persona; gestiona especialidades y sueldo.

asignatura.py: Controla cupos, alumnos inscritos y notas.

carrera.py: El contenedor principal que agrupa profesores y materias.

main.py: Script de prueba que orquesta todo el flujo.

Conceptos Clave Implementados

Herencia: Alumno y Profesor reutilizan el código de Persona

Polimorfismo: Verás que tanto alumnos como profesores tienen un método mostrar_info(), pero cada uno imprime datos diferentes según su rol.
