from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error
import time

def obtener_conexion():
    for i in range (4):
        try:
            conexion = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                port= int(os.getenv("DB_PORT",3306)),
                user= os.getenv("DB_USER"),
                password= os.getenv("DB_PASSWORD"),
                database= os.getenv("DB_NAME")
            )

            if conexion.is_connected():
                print("Se conecto correctamente a la base de datos")
                return conexion

        except Error as e:
            print(f"Intento {i + 1}: Iniciando. ({e})")
            time.sleep(5)

    raise Exception("No sé pudo volver a conectar. Intente más tarde")