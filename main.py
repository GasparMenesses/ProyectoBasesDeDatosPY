from db_conn.conn import conexion
from db_conn.conn import cursor

try:
    cursor.execute("SELECT * FROM actividad")

    for fila in cursor:
        print(fila)

except Exception as e:
    print("Error al conectar a la base de datos:", e)

finally:

    conexion.close()
