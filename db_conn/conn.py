from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

conexion = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

print("Conectado correctamente")

cursor = conexion.cursor()
