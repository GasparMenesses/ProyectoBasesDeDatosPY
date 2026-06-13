from db_conn.conn import obtener_conexion
from modelado.espacio import Espacio


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

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = """
        INSERT INTO espacio
        (nombre, ubicacion)
        VALUES (%s, %s)
    """

    valores = (
        nombre,
        ubicacion
    )

    cursor.execute(sql, valores)

    conexion.commit()

    cursor.close()
    conexion.close()