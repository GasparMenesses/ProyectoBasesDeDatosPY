class inscripcion:

    def __init__(self, id_inscripcion, est_documento, id_actividad, estado, fecha_inscripcion):
        self.id_inscripcion = id_inscripcion
        self.est_documento = est_documento
        self.id_actividad = id_actividad
        self.estado = estado
        self.fecha_inscripcion = fecha_inscripcion

    def __str__(self):
        return (f"Inscripción {self.id_inscripcion} - Estudiante {self.est_documento}  - Actividad {self.id_actividad} - {self.estado}")