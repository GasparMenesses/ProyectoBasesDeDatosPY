class estudiantes:
    def __init__ (self, documento, nombre, apellido, correo_electronico, carrera, facultad):
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.correo_electronico = correo_electronico
        self.carrera = carrera
        self.facultad = facultad

    def __str__(self):
        return f"{self.documento} - {self.nombre} {self.apellido}"
