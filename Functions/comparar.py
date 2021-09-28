def COMPARATIONS (enfermedad,cursor):
    disease_t = cursor.fetchall()
    for fila in disease_t:
        if (enfermedad == fila[1]):
            return fila[0]
    return print("Enfermedad no encontrada")