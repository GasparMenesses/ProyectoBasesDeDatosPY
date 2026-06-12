from db_conn.conn import obtener_conexión

try:
    conexion = obtener_conexión()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM actividad")

    for fila in cursor:
        print(fila)

except Exception as e:
    print("Error al conectar a la base de datos:", e)

finally:
    cursor.close()
    conexion.close()

