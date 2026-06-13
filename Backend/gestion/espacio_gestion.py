from db_conn.conn import obtener_conexion
from Backend.modelado.Espacio import Espacio

# Obtener todos los espacios
def listar_espacios():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_espacio,
               nombre,
               ubicacion
        FROM espacio
    """)

    filas = cursor.fetchall()

    espacios = []

    for fila in filas:

        espacio = Espacio(
            fila[0],  # id_espacio
            fila[1],  # nombre
            fila[2]   # ubicacion
        )

        espacios.append(espacio)

    cursor.close()
    conexion.close()

    return espacios

# Insertar un nuevo espacio
def crear_espacio(nombre, ubicacion):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO espacio (nombre, ubicacion)
            VALUES (%s, %s)
        """, (nombre, ubicacion))

        conexion.commit()
        print("Espacio creado correctamente.")

    except Exception as e:
        if conexion:
            conexion.rollback()
        print("Error al crear espacio:", e)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def modificar_espacio(id_espacio, nombre, ubicacion):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Verificar que el espacio exista
        cursor.execute("""
            SELECT id_espacio FROM espacio
            WHERE id_espacio = %s
        """, (id_espacio,))

        if cursor.fetchone() is None:
            print("El espacio no existe.")
            return

        cursor.execute("""
            UPDATE espacio
            SET nombre = %s,
                ubicacion = %s
            WHERE id_espacio = %s
        """, (nombre, ubicacion, id_espacio))

        conexion.commit()
        print("Espacio modificado correctamente.")

    except Exception as e:
        if conexion:
            conexion.rollback()
        print("Error al modificar espacio:", e)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def eliminar_espacio(id_espacio):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Verificar que el espacio exista
        cursor.execute("""
            SELECT id_espacio FROM espacio
            WHERE id_espacio = %s
        """, (id_espacio,))

        if cursor.fetchone() is None:
            print("El espacio no existe.")
            return

        # Verificar que no tenga actividades asociadas
        cursor.execute("""
            SELECT COUNT(*) FROM actividad
            WHERE id_espacio = %s
        """, (id_espacio,))

        if cursor.fetchone()[0] > 0:
            print("No se puede eliminar. El espacio tiene actividades asociadas.")
            return

        cursor.execute("""
            DELETE FROM espacio
            WHERE id_espacio = %s
        """, (id_espacio,))

        conexion.commit()
        print("Espacio eliminado correctamente.")

    except Exception as e:
        if conexion:
            conexion.rollback()
        print("Error al eliminar espacio:", e)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()