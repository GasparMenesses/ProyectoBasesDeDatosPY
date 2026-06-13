from db_conn.conn import obtener_conexion

def hacer_consulta(sql):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(sql)

    resultados = cursor.fetchall()

    cursor.close()
    conexion.close()

    return resultados