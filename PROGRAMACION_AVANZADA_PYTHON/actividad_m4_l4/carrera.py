class Carrera:
    def __init__(self, codigo, nombre, entidad):
        self._codigo = codigo
        self._nombre = nombre
        self._entidad = entidad
        self._profesores = []
        self._asignaturas = []
    
    def agregarProfesor(self, profesor):
        if profesor not in self._profesores:
            self._profesores.append(profesor)
            print(f"Profesor {profesor._nombre} agregado a {self._nombre}")
    
    def obtenerProfesor(self):
        return self._profesores
    
    def partirAsignatura(self, asignatura):
        if asignatura not in self._asignaturas:
            self._asignaturas.append(asignatura)
            print(f"Asignatura {asignatura._nombre} agregada a {self._nombre}")
    
    def mostrar_info(self):
        print(f"\n=== Carrera: {self._nombre} ===")
        print(f"Código: {self._codigo}")
        print(f"Entidad: {self._entidad}")
        print(f"Profesores: {len(self._profesores)}")
        print(f"Asignaturas: {len(self._asignaturas)}")
