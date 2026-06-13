from Backend.consultas.hacer_consultas import hacer_consulta

# Consulta 2: Actividades con cupos disponibles
def actividades_con_cupos():

    sql = """
        SELECT nombre AS nombre_actividad,
            cupo_maximo,
            COUNT(id_inscripcion) AS ocupados,
            cupo_maximo - COUNT(id_inscripcion) AS cupos_disponibles
        FROM actividad a
        LEFT JOIN inscripcion
            ON a.id_actividad = inscripcion.id_actividad
            AND inscripcion.estado = 'confirmada'
        GROUP BY a.id_actividad, a.nombre, a.cupo_maximo
        HAVING  cupos_disponibles > 0;
    """

    return hacer_consulta(sql)