#Nombre de variblaes a cambiar para la web

def insert (vector,cursor):
    return cursor.execute("INSERT INTO enfermedad (nombre) VALUES ("+vector+")")


#Para guardar un valor con la sentencia mysql se necesita que si o si sea "str" y para comparar se debe mostrar los valores
#para saber como se guardan y entonces empezar a comparar