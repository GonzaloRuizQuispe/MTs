#Insertar datos en la base de datos.

def INSERT (vector,cursor):
    cursor.execute("INSERT INTO enfermedad (nombre) VALUES ("+vector+")")
    return 0


#Para guardar un valor con la sentencia mysql se necesita que si o si sea "str" y para comparar se debe mostrar los valores
#para saber como se guardan y entonces empezar a comparar