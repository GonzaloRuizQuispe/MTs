#Nombre de variblaes a cambiar para la web

def INSERT (vector,cursor):
     cursor.execute("INSERT INTO enfermedad (nombre) VALUES ("+vector+")")

def Insertar(palabra):
    print(palabra)

def main():
    EPEP=input(str("Ingrese la palabra:  "))
    Insertar(EPEP)


#Para guardar un valor con la sentencia mysql se necesita que si o si sea "str" y para comparar se debe mostrar los valores
#para saber como se guardan y entonces empezar a comparar