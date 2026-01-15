from profesor import Profesor
from carrera import Carrera
from asignatura import Asignatura
from alumno import Alumno

def main():
    print("="*50)
    print("SISTEMA EDUCACIONAL")
    print("="*50)
    
    # Crear carrera
    carrera = Carrera("ING001", "Ingeniería Informática", "Facultad de Ingeniería")
    carrera.mostrar_info()
    
    # Crear profesores
    profesor1 = Profesor("12345678-9", "Juan", "Pérez", "juan@mail.cl", "Programación")
    profesor1._salario = 1500000
    
    profesor2 = Profesor("98765432-1", "María", "González", "maria@mail.cl", "Bases de Datos")
    profesor2._salario = 1600000
    
    # Agregar profesores a carrera
    carrera.agregarProfesor(profesor1)
    carrera.agregarProfesor(profesor2)
    
    # Crear asignaturas
    poo = Asignatura("POO101", "Programación Orientada a Objetos", 6, 30)
    bd = Asignatura("BD201", "Bases de Datos", 4, 25)
    web = Asignatura("WEB301", "Desarrollo Web", 5, 20)
    
    # Asignar asignaturas a profesores
    profesor1.asignarAsignatura(poo)
    profesor1.asignarAsignatura(web)
    profesor2.asignarAsignatura(bd)
    
    # Agregar asignaturas a carrera
    carrera.partirAsignatura(poo)
    carrera.partirAsignatura(bd)
    carrera.partirAsignatura(web)
    
    # Crear alumnos
    alumno1 = Alumno("20111222-3", "Carlos", "Rodríguez", "carlos@mail.cl", "2024001")
    alumno2 = Alumno("20333444-5", "Ana", "Martínez", "ana@mail.cl", "2024002")
    alumno3 = Alumno("20555666-7", "Pedro", "López", "pedro@mail.cl", "2024003")
    
    print("\n" + "="*50)
    print("INSCRIPCIÓN DE ALUMNOS")
    print("="*50)
    
    # Inscribir alumnos
    alumno1.InscribirAsignaturas(poo)
    alumno1.InscribirAsignaturas(bd)
    alumno1.InscribirAsignaturas(web)
    
    alumno2.InscribirAsignaturas(poo)
    alumno2.InscribirAsignaturas(bd)
    
    alumno3.InscribirAsignaturas(poo)
    alumno3.InscribirAsignaturas(web)
    
    print("\n" + "="*50)
    print("ASIGNACIÓN DE NOTAS")
    print("="*50)
    
    # Asignar notas
    poo.asignar_nota(alumno1, 6.5)
    bd.asignar_nota(alumno1, 5.8)
    web.asignar_nota(alumno1, 6.2)
    
    poo.asignar_nota(alumno2, 6.8)
    bd.asignar_nota(alumno2, 6.5)
    
    poo.asignar_nota(alumno3, 5.5)
    web.asignar_nota(alumno3, 6.0)
    
    print("\n" + "="*50)
    print("PROMEDIOS")
    print("="*50)
    
    # Calcular promedios
    print(f"{alumno1._nombre}: {alumno1.calcularPromedio():.2f}")
    print(f"{alumno2._nombre}: {alumno2.calcularPromedio():.2f}")
    print(f"{alumno3._nombre}: {alumno3.calcularPromedio():.2f}")
    
    print("\n" + "="*50)
    print("POLIMORFISMO - mismo método, distinta clase")
    print("="*50)
    
    # Polimorfismo
    personas = [profesor1, profesor2, alumno1, alumno2, alumno3]
    
    for persona in personas:
        persona.mostrar_info()
    
    print("\n" + "="*50)
    print("INFORMACIÓN DE ASIGNATURAS")
    print("="*50)
    
    poo.mostrar_info()
    bd.mostrar_info()
    web.mostrar_info()


if __name__ == "__main__":
    main()