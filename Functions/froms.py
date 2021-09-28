#Mostrar datos

def FROM (cursor,vector):
    cursor.execute("SELECT * FROM "+vector+"")
    cantidad_f = cursor.fetchall()
    for fila in cantidad_f:
        print(fila[0],fila[1])
    print("Total de registros: ",cursor.rowcount,"\n")
    return 0