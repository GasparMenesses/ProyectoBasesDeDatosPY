from db_conn.conn import obtener_conexion
from modelado.actividad import Actividad


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
def crear_actividad(nombre,
                    id_disciplina,
                    id_espacio,
                    cupo_maximo,
                    dia_semana,
                    horario_inicio,
                    horario_fin,
                    estado):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = """
        INSERT INTO actividad
        (nombre,
         id_disciplina,
         id_espacio,
         cupo_maximo,
         dia_semana,
         horario_inicio,
         horario_fin,
         estado)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    valores = (
        nombre,
        id_disciplina,
        id_espacio,
        cupo_maximo,
        dia_semana,
        horario_inicio,
        horario_fin,
        estado
    )

    cursor.execute(sql, valores)
    conexion.commit()

    cursor.close()
    conexion.close()