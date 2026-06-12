class espacio:
    def __init__(self, id_espacio, nombre, ubicacion):
        self.id_espacio = id_espacio
        self.nombre = nombre
        self.ubicacion = ubicacion

    def __str__(self):
        return f"{self.nombre} - {self.ubicacion}"