from db_conn.conn import obtener_conexion
from modelado.estudiante import Estudiante


def listar_estudiantes():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    # Consulta para obtener todos los estudiantes
    cursor.execute(""" 
        SELECT documento,
               nombre,
               apellido,
               correo_electronico,
               carrera,
               facultad
        FROM estudiantes
    """)

    filas = cursor.fetchall()
    estudiantes = [] # Lista donde se guardarán los objetos Estudiante

    for fila in filas: # Recorrer cada fila y convertirla en un objeto Estudiante
        estudiante = Estudiante(
            fila[0], #documento
            fila[1], #nombre
            fila[2], #apellido
            fila[3], #correo electronico
            fila[4], #carrera
            fila[5] #facultad
        )
        estudiantes.append(estudiante)

    cursor.close()
    conexion.close()

    return estudiantes


def crear_estudiante(documento,
                      nombre,
                      apellido,
                      correo_electronico,
                      carrera,
                      facultad):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = """
        INSERT INTO estudiantes
        (documento,
         nombre,
         apellido,
         correo_electronico,
         carrera,
         facultad)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    valores = (
        documento,
        nombre,
        apellido,
        correo_electronico,
        carrera,
        facultad
    )

    cursor.execute(sql, valores)

    conexion.commit()

    cursor.close()
    conexion.close()