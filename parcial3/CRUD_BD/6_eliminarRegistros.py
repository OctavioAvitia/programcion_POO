
from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="DELETE FROM clientes WHERE id = 1;"

    micursor.execute(sql)
    #Es necesario ejecutar el commit para que finalice el SQL con éxito
    conexion.commit()
except:
    print(f"Ocurrió un error por favor vuelva inentar más tarde")
else:
    print("Registro eliminado con éxito")