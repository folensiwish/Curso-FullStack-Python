from persona import Persona
from datetime import date

class Profesor(Persona):
    def __init__(self, rut, nombre, apellido, email, especialidad):
        super().__init__(rut, nombre, apellido, email)
        self._salario = 0.0
        self._fec_contratacion = date.today()
        self._especialidad = especialidad
        self._asignaturas = []
    
    def asignarAsignatura(self, asignatura):
        if asignatura not in self._asignaturas:
            self._asignaturas.append(asignatura)
            print(f"Asignatura {asignatura._nombre} asignada al profesor {self._nombre}")
    
    def obtenerAsignaturas(self):
        return self._asignaturas
    
    def calcularAntiguedad(self):
        hoy = date.today()
        antiguedad = hoy.year - self._fec_contratacion.year
        return antiguedad
    
    def mostrar_info(self):
        print(f"\n=== Profesor ===")
        print(f"Nombre: {self.NombreCompleto()}")
        print(f"RUT: {self._rut}")
        print(f"Especialidad: {self._especialidad}")
        print(f"Email: {self._email}")
        print(f"Salario: ${self._salario}")
        print(f"Asignaturas: {len(self._asignaturas)}")
