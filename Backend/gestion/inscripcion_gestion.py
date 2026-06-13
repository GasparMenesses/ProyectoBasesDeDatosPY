from db_conn.conn import obtener_conexion
from modelado.inscripcion import Inscripcion


# Listar todas las inscripciones
def listar_inscripciones():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_inscripcion,
               est_documento,
               id_actividad,
               estado,
               fecha_inscripcion
        FROM inscripcion
    """)

    filas = cursor.fetchall()
    inscripciones = []

    for fila in filas:

        inscripcion = Inscripcion(
            fila[0],
            fila[1],
            fila[2],
            fila[3],
            fila[4]
        )

        inscripciones.append(inscripcion)

    cursor.close()
    conexion.close()

    return inscripciones


# Inscribir a un estudiante en una actividad
def inscribir_estudiante(est_documento, id_actividad):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        # Buscar la actividad
        cursor.execute("""
            SELECT cupo_maximo, estado
            FROM actividad
            WHERE id_actividad = %s
        """, (id_actividad,))

        actividad = cursor.fetchone()

        if actividad is None:
            print("La actividad no existe.")
            return

        cupo_maximo = actividad[0]
        estado_actividad = actividad[1]

        # Validar que la actividad esté abierta
        if estado_actividad != "abierta":
            print("No se puede inscribir. La actividad no está abierta.")
            return

        # Verificar que el estudiante no esté inscripto
        cursor.execute("""
            SELECT id_inscripcion
            FROM inscripcion
            WHERE est_documento = %s
              AND id_actividad = %s
        """, (est_documento, id_actividad))

        ya_inscripto = cursor.fetchone()

        if ya_inscripto is not None:
            print("El estudiante ya está inscripto en esta actividad.")
            return

        # Contar confirmados
        cursor.execute("""
            SELECT COUNT(*)
            FROM inscripcion
            WHERE id_actividad = %s
              AND estado = 'confirmada'
        """, (id_actividad,))

        cantidad_confirmados = cursor.fetchone()[0]

        # Si hay cupo queda confirmada, si no queda en lista de espera
        if cantidad_confirmados < cupo_maximo:
            estado_inscripcion = "confirmada"
        else:
            estado_inscripcion = "lista_espera"

        # Insertar inscripción
        cursor.execute("""
            INSERT INTO inscripcion
            (est_documento, id_actividad, estado, fecha_inscripcion)
            VALUES (%s, %s, %s, NOW())
        """, (est_documento, id_actividad, estado_inscripcion))

        conexion.commit()

        print(f"Inscripción realizada. Estado: {estado_inscripcion}")

    except Exception as e:
        conexion.rollback()
        print("Error al inscribir estudiante:", e)

    finally:
        cursor.close()
        conexion.close()