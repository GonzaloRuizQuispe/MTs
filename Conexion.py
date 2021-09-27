#MySql Connector
import mysql.connector
from mysql.connector import Error
#Insertar Datos Desde Administracion

try:
    connection = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = 'Pool!Live45427752',
        db = 'db_diseases'
    )
    if connection.is_connected():
        print("Conexion Exitosa")

        cursor = connection.cursor()
        cursor.execute("SELECT database();")
        registro = cursor.fetchone()
        print("Conectado a la BD:",registro)

        cursor.execute("SELECT * FROM enfermedad")
        resultado = cursor.fetchall()

        for fila in resultado:
            print(fila[0],fila[1])
        print("Total de registros: ",cursor.rowcount)
    
except Error as ex:
    print("Error durante la conexion: ",ex)

finally:
    if connection.is_connected():
        connection.close()
        print("La conexion ha finalizado.")