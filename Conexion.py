import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='condominio'
    )
    if conexion.is_connected():
        print("Conectado exitosamente")
except Error as ex:
    print("Error durante la conexion", ex)