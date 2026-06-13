from db_conn.conn import obtener_conexion
from Backend.modelado.Asistencia import Asistencia

# Listar todas las asistencias registradas
def listar_asistencias():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_asistencia,
               id_inscripcion,
               fecha,
               asistio
        FROM asistencia
    """)

    filas = cursor.fetchall()
    asistencias = []

    for fila in filas:

        asistencia = Asistencia(
            fila[0],
            fila[1],
            fila[2],
            fila[3]
        )

        asistencias.append(asistencia)

    cursor.close()
    conexion.close()

    return asistencias


# Registrar la asistencia de una inscripción
def registrar_asistencia(id_inscripcion, fecha, asistio):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        # Verificar que la inscripción exista y esté confirmada
        cursor.execute("""
            SELECT estado
            FROM inscripcion
            WHERE id_inscripcion = %s
        """, (id_inscripcion,))

        inscripcion = cursor.fetchone()

        if inscripcion is None:
            print("La inscripción no existe.")
            return

        estado_inscripcion = inscripcion[0]

        if estado_inscripcion != "confirmada":
            print("No se puede registrar asistencia. La inscripción no está confirmada.")
            return

        # Registrar asistencia
        cursor.execute("""
            INSERT INTO asistencia
            (id_inscripcion, fecha, asistio)
            VALUES (%s, %s, %s)
        """, (id_inscripcion, fecha, asistio))

        conexion.commit()

        print("Asistencia registrada correctamente.")

    except Exception as e:
        conexion.rollback()
        print("Error al registrar asistencia:", e)

    finally:
        cursor.close()
        conexion.close()