from db_conn.conn import obtener_conexion
from modelado.estudiante import Estudiante
def listar_estudiantes():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

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
    estudiantes = []

    for fila in filas:
        estudiante = Estudiante(
            fila[0],
            fila[1],
            fila[2],
            fila[3],
            fila[4],
            fila[5]
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