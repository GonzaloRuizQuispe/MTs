from _typeshed import Self
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = 'Pool!Live45427752',
        db = 'mts'
    )
    
except Exception as ex:
    print(ex)