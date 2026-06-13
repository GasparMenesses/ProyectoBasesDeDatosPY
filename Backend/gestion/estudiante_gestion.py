from db_conn.conn import obtener_conexion
from Backend.modelado.Estudiante import Estudiante

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
            fila[0],  # documento
            fila[1],  # nombre
            fila[2],  # apellido
            fila[3],  # correo electronico
            fila[4],  # carrera
            fila[5]   # facultad
        )
        estudiantes.append(estudiante)

    cursor.close()
    conexion.close()

    return estudiantes

def crear_estudiante(documento, nombre, apellido, correo_electronico, carrera, facultad):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = """
        INSERT INTO estudiantes
        (documento, nombre, apellido, correo_electronico, carrera, facultad)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    valores = (documento, nombre, apellido, correo_electronico, carrera, facultad)

    cursor.execute(sql, valores)
    conexion.commit()

    cursor.close()
    conexion.close()


def modificar_estudiante(documento, nombre, apellido, correo_electronico, carrera, facultad):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        # Verificar que el estudiante exista
        cursor.execute("""
            SELECT documento FROM estudiantes
            WHERE documento = %s
        """, (documento,))

        if cursor.fetchone() is None:
            print("El estudiante no existe.")
            return

        cursor.execute("""
            UPDATE estudiantes
            SET nombre = %s,
                apellido = %s,
                correo_electronico = %s,
                carrera = %s,
                facultad = %s
            WHERE documento = %s
        """, (nombre, apellido, correo_electronico, carrera, facultad, documento))

        conexion.commit()
        print("Estudiante modificado correctamente.")

    except Exception as e:
        conexion.rollback()
        print("Error al modificar estudiante:", e)

    finally:
        cursor.close()
        conexion.close()

def eliminar_estudiante(documento):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        # Verificar que el estudiante exista
        cursor.execute("""
            SELECT documento FROM estudiantes
            WHERE documento = %s
        """, (documento,))

        if cursor.fetchone() is None:
            print("El estudiante no existe.")
            return

        # Verificar que no tenga inscripciones confirmadas
        cursor.execute("""
            SELECT COUNT(*) FROM inscripcion
            WHERE est_documento = %s
              AND estado = 'confirmada'
        """, (documento,))

        if cursor.fetchone()[0] > 0:
            print("No se puede eliminar. El estudiante tiene inscripciones confirmadas.")
            return

        cursor.execute("""
            DELETE FROM estudiantes
            WHERE documento = %s
        """, (documento,))

        conexion.commit()
        print("Estudiante eliminado correctamente.")

    except Exception as e:
        conexion.rollback()
        print("Error al eliminar estudiante:", e)

    finally:
        cursor.close()
        conexion.close()
