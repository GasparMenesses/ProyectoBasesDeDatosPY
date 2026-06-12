from db_conn.conn import obtener_conexion

try:
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM actividad")

    for fila in cursor:
        print(fila)

except Exception as e:
    print("Error al conectar a la base de datos:", e)

finally:
    cursor.close()
    conexion.close()

