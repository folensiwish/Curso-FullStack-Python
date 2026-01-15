class Asignatura:
    def __init__(self, codigo, nombre, horas_semanales=4, cupo_max=30):
        self._codigo = codigo
        self._nombre = nombre
        self._horas_semanales = horas_semanales
        self._cupo_max = cupo_max
        self._alumnos = []
        self._notas = {}
    
    def agregarAlumno(self, alumno):
        if len(self._alumnos) < self._cupo_max:
            if alumno not in self._alumnos:
                self._alumnos.append(alumno)
                self._notas[alumno] = 0.0
                return True
            else:
                print("El alumno ya está inscrito")
                return False
        else:
            print("Cupo lleno")
            return False
    
    def obtenerAlumnos(self):
        return self._alumnos
    
    def asignar_nota(self, alumno, nota):
        if alumno in self._alumnos:
            self._notas[alumno] = nota
            print(f"Nota {nota} asignada a {alumno._nombre}")
        else:
            print("El alumno no está inscrito")
    
    def obtener_nota_alumno(self, alumno):
        if alumno in self._notas:
            return self._notas[alumno]
        return 0.0
    
    def mostrar_info(self):
        print(f"\n=== Asignatura: {self._nombre} ===")
        print(f"Código: {self._codigo}")
        print(f"Horas: {self._horas_semanales}")
        print(f"Alumnos: {len(self._alumnos)}/{self._cupo_max}")