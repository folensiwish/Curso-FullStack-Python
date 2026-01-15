from persona import Persona

class Alumno(Persona):
    def __init__(self, rut, nombre, apellido, email, matricula):
        super().__init__(rut, nombre, apellido, email)
        self._promedio = 0.0
        self._matricula = matricula
        self._asignaturas = []
    
    def InscribirAsignaturas(self, asignatura):
        if asignatura not in self._asignaturas:
            self._asignaturas.append(asignatura)
            asignatura.agregarAlumno(self)
            print(f"Alumno {self._nombre} inscrito en {asignatura._nombre}")
        else:
            print(f"Ya estás inscrito en esta asignatura")
    
    def calcularPromedio(self):
        if len(self._asignaturas) == 0:
            return 0.0
        
        suma = 0
        for asig in self._asignaturas:
            suma += asig.obtener_nota_alumno(self)
        
        self._promedio = suma / len(self._asignaturas)
        return self._promedio
    
    def listaAsignaturas(self):
        return self._asignaturas
    
    def mostrar_info(self):
        print(f"\n=== Alumno ===")
        print(f"Nombre: {self.NombreCompleto()}")
        print(f"RUT: {self._rut}")
        print(f"Matrícula: {self._matricula}")
        print(f"Email: {self._email}")
        print(f"Promedio: {self._promedio}")
        print(f"Asignaturas: {len(self._asignaturas)}")
