from Backend.consultas.hacer_consultas import hacer_consulta

# Consulta 1:Actividades con mayor cantidad de inscriptos confirmados
def actividades_mayor_inscriptos():

    sql = """
        SELECT 
            a.nombre AS nombre_actividad, COUNT(i.id_inscripcion) AS cantidad_de_inscriptos
        FROM actividad a
        LEFT JOIN inscripcion i
            ON a.id_actividad = i.id_actividad AND i.estado = 'confirmada'
        GROUP BY a.id_actividad, a.nombre
        ORDER BY cantidad_de_inscriptos DESC
    """

    return hacer_consulta(sql)