class disciplina:
    def __init__(self, id_disciplina, nombre):
        self.id_disciplina = id_disciplina
        self.nombre = nombre

    def __str__(self):
        return self.nombre