def comparar (enfermedad,cursor):
    symptons = cursor.fetchall()
    for fila in symptons:
        if (symptons == fila[2])
            return fila[0]
        else
            return print("Enfermedad no encontrada")