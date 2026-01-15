from datetime import date

class Persona:
    def __init__(self, rut, nombre, apellido, email, celular=""):
        self._rut = rut
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._celular = celular
        self._fec_nacimiento = None
    
    def NombreCompleto(self):
        return f"{self._nombre} {self._apellido}"
    
    def ActualizarEmail(self, nuevo_email):
        self._email = nuevo_email
        print(f"Email actualizado a: {nuevo_email}")
    
    def CalcularEdad(self):
        if self._fec_nacimiento:
            hoy = date.today()
            edad = hoy.year - self._fec_nacimiento.year
            return edad
        return 0