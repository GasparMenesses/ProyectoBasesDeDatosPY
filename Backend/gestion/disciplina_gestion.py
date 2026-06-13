from db_conn.conn import obtener_conexion
from modelado.disciplina import Disciplina


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