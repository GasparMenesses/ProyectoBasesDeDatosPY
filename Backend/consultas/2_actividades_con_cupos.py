from Backend.consultas.hacer_consultas import hacer_consulta

# Consulta 2: Actividades con cupos disponibles
def actividades_con_cupos():

    sql = """
        SELECT
            a.nombre AS nombre_actividad,
            a.cupo_maximo,
            COUNT(i.id_inscripcion) AS ocupados,
            a.cupo_maximo - COUNT(i.id_inscripcion) AS cupos_disponibles
        FROM actividad a
        LEFT JOIN inscripcion i
            ON a.id_actividad = i.id_actividad
            AND i.estado = 'confirmada'
        GROUP BY a.id_actividad, a.nombre, a.cupo_maximo
        HAVING cupos_disponibles > 0
    """

    return hacer_consulta(sql)