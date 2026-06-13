from db_conn.conn import obtener_conexion
from Backend.modelado.Actividad import Actividad

# Obtener todas las actividades deportivas
def listar_actividades():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_actividad,
               nombre,
               id_disciplina,
               id_espacio,
               cupo_maximo,
               dia_semana,
               horario_inicio,
               horario_fin,
               estado
        FROM actividad
    """)

    filas = cursor.fetchall()
    actividades = []

    for fila in filas:
        actividad = Actividad(
            fila[0],  # id_actividad
            fila[1],  # nombre
            fila[2],  # id_disciplina
            fila[3],  # id_espacio
            fila[4],  # cupo_maximo
            fila[5],  # dia_semana
            fila[6],  # horario_inicio
            fila[7],  # horario_fin
            fila[8]   # estado
        )
        actividades.append(actividad)

    cursor.close()
    conexion.close()

    return actividades

# Agregar una nueva actividad deportiva
def crear_actividad(nombre, id_disciplina, id_espacio, cupo_maximo,
                    dia_semana, horario_inicio, horario_fin, estado):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO actividad
            (nombre, id_disciplina, id_espacio, cupo_maximo,
             dia_semana, horario_inicio, horario_fin, estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (nombre, id_disciplina, id_espacio, cupo_maximo,
              dia_semana, horario_inicio, horario_fin, estado))

        conexion.commit()
        print("Actividad creada correctamente.")

    except Exception as e:
        if conexion:
            conexion.rollback()
        print("Error al crear actividad:", e)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()


def modificar_actividad(id_actividad, nombre, id_disciplina, id_espacio, cupo_maximo,
                        dia_semana, horario_inicio, horario_fin, estado):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Verificar que la actividad exista
        cursor.execute("""
            SELECT id_actividad FROM actividad
            WHERE id_actividad = %s
        """, (id_actividad,))

        if cursor.fetchone() is None:
            print("La actividad no existe.")
            return

        cursor.execute("""
            UPDATE actividad
            SET nombre = %s,
                id_disciplina = %s,
                id_espacio = %s,
                cupo_maximo = %s,
                dia_semana = %s,
                horario_inicio = %s,
                horario_fin = %s,
                estado = %s
            WHERE id_actividad = %s
        """, (nombre, id_disciplina, id_espacio, cupo_maximo,
              dia_semana, horario_inicio, horario_fin, estado, id_actividad))

        conexion.commit()
        print("Actividad modificada correctamente.")

    except Exception as e:
        if conexion:
            conexion.rollback()
        print("Error al modificar actividad:", e)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def cambiar_estado_actividad(id_actividad, nuevo_estado):
    estados_validos = ("abierta", "cerrada", "finalizada", "cancelada")

    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        if nuevo_estado not in estados_validos:
            print(f"Estado inválido. Los estados posibles son: {', '.join(estados_validos)}")
            return

        # Verificar que la actividad exista
        cursor.execute("""
            SELECT id_actividad FROM actividad
            WHERE id_actividad = %s
        """, (id_actividad,))

        if cursor.fetchone() is None:
            print("La actividad no existe.")
            return

        cursor.execute("""
            UPDATE actividad
            SET estado = %s
            WHERE id_actividad = %s
        """, (nuevo_estado, id_actividad))

        conexion.commit()
        print(f"Estado de actividad actualizado a '{nuevo_estado}'.")

    except Exception as e:
        if conexion:
            conexion.rollback()
        print("Error al cambiar estado de actividad:", e)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()


def eliminar_actividad(id_actividad):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Verificar que la actividad exista
        cursor.execute("""
            SELECT id_actividad FROM actividad
            WHERE id_actividad = %s
        """, (id_actividad,))

        if cursor.fetchone() is None:
            print("La actividad no existe.")
            return

        # Verificar que no tenga inscripciones confirmadas
        cursor.execute("""
            SELECT COUNT(*) FROM inscripcion
            WHERE id_actividad = %s
              AND estado = 'confirmada'
        """, (id_actividad,))

        if cursor.fetchone()[0] > 0:
            print("No se puede eliminar. La actividad tiene inscripciones confirmadas.")
            return

        cursor.execute("""
            DELETE FROM actividad
            WHERE id_actividad = %s
        """, (id_actividad,))

        conexion.commit()
        print("Actividad eliminada correctamente.")

    except Exception as e:
        if conexion:
            conexion.rollback()
        print("Error al eliminar actividad:", e)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()
    cursor.execute(sql, valores)
    conexion.commit()

    cursor.close()
    conexion.close()