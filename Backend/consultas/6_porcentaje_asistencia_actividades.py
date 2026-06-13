from Backend.consultas.hacer_consultas import hacer_consulta

# Consulta 6: Porcentaje de asistencia por actividad
def consulta_6_porcentaje_asistencia_actividades():

    sql = """
        SELECT
            ac.nombre AS nombre_actividad,
            COUNT(asist.id_asistencia) AS asistencias_registradas,
            SUM(asist.asistio) AS asistencias,
            COUNT(asist.id_asistencia) - SUM(asist.asistio) AS inasistencias,
            (SUM(asist.asistio) * 100) / COUNT(asist.id_asistencia) AS porcentaje
        FROM actividad ac
        LEFT JOIN inscripcion i
            ON ac.id_actividad = i.id_actividad
        LEFT JOIN asistencia asist
            ON i.id_inscripcion = asist.id_inscripcion
        GROUP BY ac.nombre
        ORDER BY porcentaje DESC
    """

    return hacer_consulta(sql)