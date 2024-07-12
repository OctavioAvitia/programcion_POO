
from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="SELECT * FROM  clientes"

    micursor.execute(sql)

    resultado=micursor.fetchall()

    for fila in resultado:
    
        print(f"Id: {fila[0]} | Nombre: {fila[1]} | Dirección: {fila[2]} | Telefono: {fila[3]}")
except:
    print(f"Ocurrió un error por favor vuelva inentar más tarde...")
else:
    print("Registros consultados con éxito")