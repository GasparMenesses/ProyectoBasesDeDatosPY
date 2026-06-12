class asistencia:

    def __init__(self, id_asistencia, id_inscripcion, fecha, asistio):
        self.id_asistencia = id_asistencia
        self.id_inscripcion = id_inscripcion
        self.fecha = fecha
        self.asistio = asistio

    def __str__(self):
        estado = "Asistió" if self.asistio else "No asistió"
        return f"Asistencia {self.id_asistencia} - Inscripción {self.id_inscripcion} - {self.fecha} - {estado}"