# Importamos Flask para crear la aplicación web y render_template para mostrar archivos HTML
from flask import Flask, render_template

# Creamos la aplicación Flask
app = Flask(__name__)

# Ruta principal del sitio
@app.route("/")
def inicio():

    # Muestra el archivo index.html
    return render_template("index.html")

# Verifica que este archivo sea el que se está ejecutando directamente y no importado desde otro módulo
if __name__ == "__main__":

    # Inicia el servidor Flask
    # debug=True permite ver errores detallados y
    # reiniciar automáticamente cuando guardamos cambios
    app.run(debug=True)


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
    conexion.close()

from flask import Flask, jsonify

from asistencia_gestion import listar_asistencias, registrar_asistencia
from disciplina gestion import listar_disciplinas, crear_disciplinas
"""


