from Backend.consultas.hacer_consultas import hacer_consulta

# Consulta 5: Porcentaje de ocupación de cada actividad
def consulta_5_porcentaje_ocupacion_actividades():

    sql = """
        SELECT
            a.nombre AS nombre_actividad,
            a.cupo_maximo,
            COUNT(i.id_inscripcion) AS cupos_ocupados,
            a.cupo_maximo - COUNT(i.id_inscripcion) AS cupos_disponibles,
            (COUNT(i.id_inscripcion) * 100) / a.cupo_maximo AS porcentaje_ocupacion_
        FROM actividad a
        LEFT JOIN inscripcion i
            ON a.id_actividad = i.id_actividad
            AND i.estado = 'confirmada'
        GROUP BY a.nombre, a.cupo_maximo
        ORDER BY 5 DESC;
    """

    return hacer_consulta(sql)