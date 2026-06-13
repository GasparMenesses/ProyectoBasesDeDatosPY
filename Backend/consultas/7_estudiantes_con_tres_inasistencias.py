from Backend.consultas.hacer_consultas import hacer_consulta

# Consulta 7: Estudiantes con tres o más inasistencias registradas
def consulta_7_estudiantes_con_tres_inasistencias():

    sql = """
        SELECT documento, nombre, apellido, COUNT(id_asistencia) AS inasistencias
        FROM estudiantes
        JOIN inscripcion i ON documento = est_documento
        JOIN asistencia ON i.id_inscripcion = asistencia.id_inscripcion
        WHERE asistio = FALSE
        GROUP BY documento, nombre, apellido
        HAVING inasistencias >= 3;
    """

    return hacer_consulta(sql)