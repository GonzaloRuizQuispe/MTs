import mysql.connector
from mysql.connector import Error

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
        infoServer = connection.get_server_info()
        print("Info del servidor:",infoServer)
    
except Error as ex:
    print("Error durante la conexion: ",ex)

finally:
    if connection.is_connected():
        connection.close()
        print("La conexion ha finalizado.")