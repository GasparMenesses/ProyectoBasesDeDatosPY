class actividad:
    def __init__ (self, id_actividad, nombre, id_disciplina, id_espacio, cupo_maximo,
                  dia_semana, horario_inicio, horario_fin, estado):
        self.id_actividad = id_actividad
        self.nombre = nombre
        self.id_disciplina = id_disciplina
        self.id_espacio = id_espacio
        self.cupo_maximo = cupo_maximo
        self.dia_semana = dia_semana
        self.horario_inicio = horario_inicio
        self.horario_fin = horario_fin
        self.estado = estado

    def __str__(self):
        return f"{self.nombre} ({self.estado})"
