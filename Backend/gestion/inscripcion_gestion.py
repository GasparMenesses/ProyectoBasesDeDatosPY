from db_conn.conn import obtener_conexion
from Backend.modelado.Inscripción import Inscripcion

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
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

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

        if cursor.fetchone() is not None:
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

        cursor.execute("""
            INSERT INTO inscripcion
            (est_documento, id_actividad, estado, fecha_inscripcion)
            VALUES (%s, %s, %s, NOW())
        """, (est_documento, id_actividad, estado_inscripcion))

        conexion.commit()
        print(f"Inscripción realizada. Estado: {estado_inscripcion}")

    except Exception as e:
        if conexion:
            conexion.rollback()
        print("Error al inscribir estudiante:", e)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def cancelar_inscripcion(id_inscripcion):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Verificar que la inscripción exista
        cursor.execute("""
            SELECT estado, id_actividad
            FROM inscripcion
            WHERE id_inscripcion = %s
        """, (id_inscripcion,))

        inscripcion = cursor.fetchone()

        if inscripcion is None:
            print("La inscripción no existe.")
            return

        estado_actual = inscripcion[0]
        id_actividad = inscripcion[1]

        # Cancelar la inscripción
        cursor.execute("""
            UPDATE inscripcion
            SET estado = 'cancelada'
            WHERE id_inscripcion = %s
        """, (id_inscripcion,))

        # Si era confirmada, promover el primero de lista de espera
        if estado_actual == "confirmada":
            cursor.execute("""
                SELECT id_inscripcion
                FROM inscripcion
                WHERE id_actividad = %s
                  AND estado = 'lista_espera'
                ORDER BY fecha_inscripcion ASC
                LIMIT 1
            """, (id_actividad,))

            siguiente = cursor.fetchone()

            if siguiente is not None:
                cursor.execute("""
                    DELETE FROM inscripcion
                    WHERE id_inscripcion = %s       
                """, (siguiente[0],))
                print("Se promovió al siguiente estudiante de lista de espera.")

        conexion.commit()
        print("Inscripción cancelada correctamente.")

    except Exception as e:
        if conexion:
            conexion.rollback()
        print("Error al cancelar inscripción:", e)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()