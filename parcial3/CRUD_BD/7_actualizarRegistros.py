
from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="UPDATE clientes SET direccion = 'Col. del UTD' where id=11;"

    micursor.execute(sql)
    #Es necesario ejecutar el commit para que finalice el SQL con éxito
    conexion.commit()
except:
    print(f"Ocurrió un error por favor vuelva inentar más tarde")
else:
    print("Registro actualizado con éxito")