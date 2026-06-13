from Backend.consultas.hacer_consultas import hacer_consulta

# Consulta 3: Cantidad de inscriptos por disciplina deportiva
def consulta_3_inscriptos_por_disciplina():

    sql = """
        SELECT
            dd.nombre AS nombre_disciplina,
            COUNT(i.id_inscripcion) AS cantidad_inscriptos
        FROM disciplina_deportiva dd
        LEFT JOIN actividad a
            ON dd.id_disciplina = a.id_disciplina
        LEFT JOIN inscripcion i
            ON a.id_actividad = i.id_actividad
            AND i.estado = 'confirmada'
        GROUP BY dd.id_disciplina, dd.nombre
    """

    return hacer_consulta(sql)