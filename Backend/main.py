"""from db_conn.conn import obtener_conexion

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
    conexion.close() """

from flask import Flask, jsonify

from asistencia_gestion import listar_asistencias, registrar_asistencia
from disciplina gestion import listar_disciplinas, crear_disciplinas

