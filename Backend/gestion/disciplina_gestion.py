from db_conn.conn import obtener_conexion
from Backend.modelado.Disciplina import Disciplina

# Obtener todas las disciplinas deportivas
def listar_disciplinas():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_disciplina,
               nombre
        FROM disciplina_deportiva
    """)

    filas = cursor.fetchall()
    disciplinas = []

    for fila in filas:

        disciplina = Disciplina(
            fila[0],  # id_disciplina
            fila[1]   # nombre
        )
        disciplinas.append(disciplina)

    cursor.close()
    conexion.close()

    return disciplinas

# Insertar una nueva disciplina deportiva
def crear_disciplina(nombre):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = """
        INSERT INTO disciplina_deportiva
        (nombre)
        VALUES (%s)
    """

    valores = (nombre,)

    cursor.execute(sql, valores)
    conexion.commit()

    cursor.close()
    conexion.close()


def modificar_disciplina(id_disciplina, nombre):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Verificar que la disciplina exista
        cursor.execute("""
            SELECT id_disciplina FROM disciplina_deportiva
            WHERE id_disciplina = %s
        """, (id_disciplina,))

        if cursor.fetchone() is None:
            print("La disciplina no existe.")
            return

        cursor.execute("""
            UPDATE disciplina_deportiva
            SET nombre = %s
            WHERE id_disciplina = %s
        """, (nombre, id_disciplina))

        conexion.commit()
        print("Disciplina modificada correctamente.")

    except Exception as e:
        if conexion:
            conexion.rollback()
        print("Error al modificar disciplina:", e)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def eliminar_disciplina(id_disciplina):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Verificar que la disciplina exista
        cursor.execute("""
            SELECT id_disciplina FROM disciplina_deportiva
            WHERE id_disciplina = %s
        """, (id_disciplina,))

        if cursor.fetchone() is None:
            print("La disciplina no existe.")
            return

        # Verificar que no tenga actividades asociadas
        cursor.execute("""
            SELECT COUNT(*) FROM actividad
            WHERE id_disciplina = %s
        """, (id_disciplina,))

        if cursor.fetchone()[0] > 0:
            print("No se puede eliminar. La disciplina tiene actividades asociadas.")
            return

        cursor.execute("""
            DELETE FROM disciplina_deportiva
            WHERE id_disciplina = %s
        """, (id_disciplina,))

        conexion.commit()
        print("Disciplina eliminada correctamente.")

    except Exception as e:
        if conexion:
            conexion.rollback()
        print("Error al eliminar disciplina:", e)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()