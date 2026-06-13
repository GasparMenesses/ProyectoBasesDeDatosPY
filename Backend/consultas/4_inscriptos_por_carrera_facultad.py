from Backend.consultas.hacer_consultas import hacer_consulta

# Consulta 4: Cantidad de inscriptos por carrera o facultad
def consulta_4_inscriptos_por_carrera_facultad():

    sql = """
        SELECT
            e.carrera AS nombre_carrera,
            e.facultad AS facultad,
            COUNT(DISTINCT e.documento) AS cantidad_inscriptos
        FROM estudiantes e
        LEFT JOIN inscripcion i
            ON e.documento = i.est_documento
            AND i.estado = 'confirmada'
        GROUP BY e.carrera, e.facultad
        ORDER BY cantidad_inscriptos DESC
    """

    return hacer_consulta(sql)