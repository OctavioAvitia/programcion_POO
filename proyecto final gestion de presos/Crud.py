import mysql.connector
#SI FUNCIONA !!NO LE MUEVAS!!
#Conexion con la BD de MySQL
conecction=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestion_de_presos"
)
cursor = conecction.cursor()
#Edgar lo que vas a hacer es encargarte de hacer las funciones de registrar
class Preso:
    def __init__(self):
        self.presos = "presos"
        
    def secuencia_menu(self):
        while True:
            x = self.menu()#esta es una variable que abre nuestro menu y segun lo que escojas es lo que se va a ejecutar
            match x:#parecido al while true lo que hace es que segun el valor de x te va a escojer una opcion y la va a ejecutar
                case "1":
                    self.registrar()
                case "2":
                    self.editar()
                case "3":
                    self.eliminar()
                case "4":
                    self.consulta()
                case "5":
                    break
                case _:
                    print("Favor de escribir una opcion valida")

    def menu(self):#SI FUNCIONA !!NO LE MUEVAS!!
        print("_________________________________________")
        print(f"|{self.presos.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|1)Registrar                            |")
        print("|2)Editar                               |")
        print("|3)eliminar                             |")
        print("|4)consultar                            |")
        print("|5)salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?")

    def registrar(self):
        Nombre= input("inserte el nombre del preso: ")
        Años_carcel= input("ingrese el tiempo de la condena: ")
        Zona_Celda= input("ingrese la area asignada del preso: ")
        Crimen= input("ingrese el crimen del preso: ")
        query = "INSERT INTO preso (Nombre,Años_Carcel,Zona_Celda,Crimen) VALUES (%s,%s,%s,%s)"
        cursor.execute(query, (Nombre,Años_carcel,Zona_Celda,Crimen))
        conecction.commit()
        print("se relaizo correctamente el registro...")

    def editar(self):
        self.consulta()
        id = input("Ingrese id del preso a editar:")
        cursor.execute("SELECT * FROM `preso` WHERE id = %s;",(id,))
        resultado = cursor.fetchall()

        print(f"id del preso {resultado[0][0]}")
        print(f"Nombre del preso {resultado[0][1]}")
        Nombre = input("Ingrese el Nombre del preso: ")
        print(f"Años de carcel{resultado[0][2]}")
        Años_carcel = input("Ingrese los años de carcel: ")
        print(f"zona de la celda {resultado[0][3]}")
        Zona_Celda = input("Ingrese la Zona nueva: ")
        print(f"Crimen del preso {resultado[0][4]}")
        Crimen = input("Ingrese el Crimen cometido: ")
        comando = "UPDATE preso SET id=%s,Nombre=%s,Años_Carcel=%s,Zona_Celda=%s,Crimen=%s WHERE id =%s"
        cursor.execute(comando, (Nombre,Años_carcel,Zona_Celda,Crimen))
        conecction.commit()
        print("------------------------------------")
        print("edicion completada")
        

    def eliminar(self):
        self.consulta()
        id = input("ingresar el id del preso a eliminar:")
        borrar = f"DELETE FROM preso WHERE id = {id}"
        cursor.execute(borrar)
        conecction.commit()
        print("Preso eliminado correctamente")

    def consulta(self):
        cursor.execute("SELECT * FROM preso")
        Mostrar = cursor.fetchall()
        print("---------------------------------------")
        if Mostrar:
            for fila in Mostrar:
                print(f"id del preso {fila[0]}")
                print(f"Nombre del preso: {fila[1]}")
                print(f"Años de carcel: {fila[2]}")
                print(f"Zona celda: {fila[3]}")
                print(f"Crimen cometido: {fila[4]}")
                print("--------------------------------------------------------")
        else:
            print("no hay datos disponibles")
#SI FUNCIONA !!NO LE MUEVAS!!
#aqui igual perra
class Celda:
    def __init__(self):#SI FUNCIONA !!NO LE MUEVAS!!
        self.celda = "celda"
        self.consulta_especial = "Distribuidor de tienda"
        
    def secuencia_menu(self):
        while True:
            x = self.menu()#esta es una variable que abre nuestro menu y segun lo que escojas es lo que se va a ejecutar
            match x:#parecido al while true lo que hace es que segun el valor de x te va a escojer una opcion y la va a ejecutar
                case "1":
                    self.registrar()
                case "2":
                    self.editar()
                case "3":
                    self.eliminar()
                case "4":
                    self.consulta()
                case "5":
                    break
                case _:
                    print("Favor de escribir una opcion valida")
            
    def menu(self):#SI FUNCIONA !!NO LE MUEVAS!!
        print("_________________________________________")
        print(f"|{self.celda.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|1)Registrar                            |")
        print("|2)Editar                               |")
        print("|3)eliminar                             |")
        print("|4)consultar                            |")
        print("|5)salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?")

    def registrar(self):
        Zona_celda = input("inserte la Zona de la celda: ")
        Numero = input("Ingrese el numero de celda: ")
        ubicacion = input("Ingrese la ubicacion: ")
        query = "INSERT INTO ubicacion (Zona_Celda, Numero, Ubicacion) VALUES (%s, %s, %s)"
        #aqui se va a poner los datos que estan punteados
        cursor.execute(query, (Zona_celda,Numero,ubicacion))
        conecction.commit()
        print("se relaizo correctamente el registro...")

    def editar(self):
        self.consulta()
        id = input("Ingrese id del preso a editar:")
        cursor.execute("SELECT * FROM ubicacion WHERE id = %s;",(id,))
        resultado = cursor.fetchall()

        print(f"id de la ubicacion {resultado[0][0]}")
        print(f"Zona celda {resultado[0][1]}")
        Zona_Celda = input("Ingrese la zona de la celda: ")
        print(f"Numero de Celda{resultado[0][2]}")
        Numero = input("Numero de carcel: ")
        print(f"Ubicacion de la celda {resultado[0][3]}")
        ubicacion = input("Ingrese la ubicacion dela celda: ")
        comando = "UPDATE ubicacion SET Zona_celda = %s,Numero = %s,Ubicacion = %s WHERE id = %s"
        cursor.execute(comando,(Zona_Celda,Numero,ubicacion))
        conecction.commit()
        print("------------------------------------")

    def eliminar(self):
        celda.consultar()
        id = input("ingresar el id a borrar:")
        comando = "DELETE FROM ubicacion WHERE id = %s"
        cursor.execute(comando, (id,))
        conecction.commit()
        print("se a eliminado exitosamente")
        pass

    def consulta(self):
        cursor.execute("SELECT * FROM ubicacion")
        Mostrar = cursor.fetchall()
        print("---------------------------------------")
        if Mostrar:
            for fila in Mostrar:
                print(f"id de celda {fila[0]}")
                print(f"Zona celda: {fila[1]}")
                print(f"Numero de celda: {fila[2]}")
                print(f"Ubicacion de celda: {fila[3]}")
                print("--------------------------------------------------------")
        else:
            print("no hay datos disponibles")

class Crimen():
    def __init__(self):
        self.crimen = "Crimen"

    def secuencia_menu(self):
        while True:
            x = self.menu()#esta es una variable que abre nuestro menu y segun lo que escojas es lo que se va a ejecutar
            match x:#parecido al while true lo que hace es que segun el valor de x te va a escojer una opcion y la va a ejecutar
                case "1":
                    self.registrar()
                case "2":
                    self.editar()
                case "3":
                    self.eliminar()
                case "4":
                    self.consulta()
                case "5":
                    break
                case _:
                    print("Favor de escribir una opcion valida")
            
    def menu(self):#SI FUNCIONA !!NO LE MUEVAS!!
        print("_________________________________________")
        print(f"|{self.crimen.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|1)Registrar                            |")
        print("|2)Editar                               |")
        print("|3)eliminar                             |")
        print("|4)consultar                            |")
        print("|5)salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?")
    
    def registrar(self):
        Tipo_Crimen = input("Ingrese el crimen cometido: ")
        Condena_Crimen = input("Ingrese la condena que se le dara: ")
        Zona_Celda = int(input("Ingrese la Ubicacion a la que va:(ingrese numero del zona ):"))
        query = "INSERT INTO crimenes (Tipo_Crimen,Condena_Crimen,Zona_Celda) VALUES (%s,%s,%s)"
        cursor.execute(query, (Tipo_Crimen,Condena_Crimen,Zona_Celda))
        conecction.commit()
        print("se relaizo correctamente el registro...")

    def editar(self):
        self.consulta()
        id = input("Ingrese Id del crimen a Editar: ")
        cursor.execute("SELECT *FROM crimenes WHERE id = %s;", (id,))
        resultado = cursor.fetchall()

        print(f"id del crimen{resultado[0][0]}")
        print(f"El tipo de crimen es {resultado[0][1]}")
        Tipo_Crimen = input("Ingrese el crimen cometido: ")
        print(f"La condena que se le dara es de: {resultado[0][2]}")
        Condena_Crimen = input("Ingrese la condena que se le dara: ")
        print(f"Ingrese el numero de zona a la que ira {resultado[0][3]}")
        Zona_Celda = int(input("Ingrese la Ubicacion a la que va:(ingrese numero del zona ):"))
        comando = "UPDATE preso SET Tipo_Crimen=%s,Condena_Crimen =%s,Zona_Celda=%s WHERE id =%s"
        cursor.execute(comando, (Tipo_Crimen,Condena_Crimen,Zona_Celda))
        conecction.commit()
        print("------------------------------------")
        print("edicion completada")

    def eliminar(self):
        crimen.consultar()
        id = input("ingresar el id a borrar:")
        comando = "DELETE FROM crimenes WHERE id = %s"
        cursor.execute(comando, (id,))
        conecction.commit()
        print("se a eliminado exitosamente")
        pass

    def consulta(self):
        cursor.execute("SELECT * FROM crimenes")
        Mostrar = cursor.fetchall()
        print("---------------------------------------")
        if Mostrar:
            for fila in Mostrar:
                print(f"id del crimen{Mostrar[0]}")
                print(f"El tipo de crimen es {Mostrar[0][1]}")
                print(f"La condena que se le dara es de: {Mostrar[0][2]}")
                print(f"el numero de zona a la que ira es {Mostrar[0][3]}")
                print("--------------------------------------------------------")
        else:
            print("no hay datos disponibles")

class Guardias():
    def __init__(self):
        self.guardia = "Guardias"

    def secuencia_menu(self):
        while True:
            x = self.menu()#esta es una variable que abre nuestro menu y segun lo que escojas es lo que se va a ejecutar
            match x:#parecido al while true lo que hace es que segun el valor de x te va a escojer una opcion y la va a ejecutar
                case "1":
                    self.registrar()
                case "2":
                    self.editar()
                case "3":
                    self.eliminar()
                case "4":
                    self.consulta()
                case "5":
                    break
                case _:
                    print("Favor de escribir una opcion valida")
            
    def menu(self):#SI FUNCIONA !!NO LE MUEVAS!!
        print("_________________________________________")
        print(f"|{self.guardia.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|1)Registrar                            |")
        print("|2)Editar                               |")
        print("|3)eliminar                             |")
        print("|4)consultar                            |")
        print("|5)salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?")
    
    def editar(self):
        self.consulta()
        id = input("Ingrese Id del guardia a Editar: ")
        cursor.execute("SELECT * FROM guardias WHERE id = %s;", (id,))
        resultado = cursor.fetchall()

        if not resultado:
            print("No se encontró un guardia con ese ID.")
            return

        print(f"id del Guardia {resultado[0][0]}")
        print(f"El Nombre del guardia es {resultado[0][1]}")
        Nombre = input("Ingrese el nombre del guardia: ")
        print(f"La zona asiganda es : {resultado[0][2]}")
        Zona_Asig = input("Ingrese la zona Asignada: ")
        print(f"El turno de trabajo al que ira {resultado[0][3]}")
        Turno = input("Ingrese el turno de trabajo: ")

        comando = "UPDATE guardias SET Nombre = %s, Zona_Asig = %s, Turno = %s WHERE id = %s"
        cursor.execute(comando, (Nombre, Zona_Asig, Turno, id))
        conecction.commit()
        print("------------------------------------")
        print("Edición completada.")


    def eliminar(self):
        guardias.consulta()
        id = input("ingresar el id a borrar:")
        comando = "DELETE FROM guardias WHERE id = %s"
        cursor.execute(comando, (id,))
        conecction.commit()
        print("se a eliminado exitosamente")
        pass

    def consulta(self):
        cursor.execute("SELECT * FROM guardias")
        Mostrar = cursor.fetchall()
        print("---------------------------------------")
        if Mostrar:
            for fila in Mostrar:
                print(f"id del guardia {Mostrar[0][0]}")
                print(f"El nombre del guardia es {Mostrar[0][1]}")
                print(f"La zona asignada es {Mostrar[0][2]}")
                print(f"El turno asignado es {Mostrar[0][3]}")
                print("--------------------------------------------------------")
        else:
                print("no hay datos disponibles")

class LiberCondi():
    def __init__(self) -> None:
        self.libercondi = "Libertad condicional"

    def secuencia_menu(self):
        while True:
            x = self.menu()#esta es una variable que abre nuestro menu y segun lo que escojas es lo que se va a ejecutar
            match x:#parecido al while true lo que hace es que segun el valor de x te va a escojer una opcion y la va a ejecutar
                case "1":
                    self.registrar()
                case "2":
                    self.editar()
                case "3":
                    self.eliminar()
                case "4":
                    self.consulta()
                case "5":
                    break
                case _:
                    print("Favor de escribir una opcion valida")
            
    def menu(self):#SI FUNCIONA !!NO LE MUEVAS!!
        print("_________________________________________")
        print(f"|{self.libercondi.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|1)Registrar                            |")
        print("|2)Editar                               |")
        print("|3)eliminar                             |")
        print("|4)consultar                            |")
        print("|5)salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer? ")
    
    def registrar(self):
        Nombre = input("Ingrese el Nombre del preso: ")
        Cadena_Cumplida = input("Ingrese tiempo de cadena cumplida: ")
        Libertad_Condicional = input("Ingrese la razon de la libertad condicional: ")
        query = "INSERT INTO libertad_condicional (Nombre,Cadena_Cumplida,Libertad_Condicional) Values (%s,%s,%s)"
        #aqui se va a poner los datos que estan punteados
        cursor.execute(query, (Nombre,Cadena_Cumplida,Libertad_Condicional))
        conecction.commit()
        print("se relaizo correctamente el registro...")

    def editar(self):
        self.consulta()
        id = input("ingrese el id del Preso a Editar")
        cursor.execute("SELECT * FROM libertad_condicional WHERE id =%s;",(id ,))
        resultado = cursor.fetchall()

        print(f"Id del Preso {resultado[0][0]}")
        print(f"El nombre del Preso a editar {resultado[0][1]}")
        Nombre = input("Ingrese el Nombre del preso: ")
        print(f"Tiempo de cadena cumplida a cambiar {resultado[0][2]}")
        Cadena_Cumplida = input("Ingrese tiempo de cadena cumplida: ")
        print(f"La razon de libertad condicional es {resultado[0][3]}")
        Libertad_Condicional = input("Ingrese la razon de la libertad condicional: ")
        comando = "UPDATE libertad_condicional SET Nombre = %s, Cadena_Cumplida = %s, Libertad_Condicional = %s WHERE id = %s"
        cursor.execute(comando, (Nombre, Cadena_Cumplida,Libertad_Condicional, id))
        conecction.commit()
        print("------------------------------------")
        print("edicion completada")

    def eliminar(self):
        libercondi.consulta()
        id = input("ingresar el id a borrar:")
        comando = "DELETE FROM Libertad_Condicional WHERE id = %s"
        cursor.execute(comando, (id,))
        conecction.commit()
        print("se  eliminada exitosamente")
        pass

    def consulta(self):
        cursor.execute("SELECT * FROM libertad_condicional")
        Mostrar = cursor.fetchall()
        print("---------------------------------------")
        if Mostrar:
            for fila in Mostrar:
                print(f"id del preso {fila[0]}")
                print(f"Nombre del preso: {fila[1]}")
                print(f"Años de carcel cumplidos: {fila[2]}")
                print(f"Razon de Libertad {fila[3]}")
                print("--------------------------------------------------------")
        else:
            print("no hay datos disponibles")

class Ubicacion():
    def __init__(self) -> None:
        self.ubicacion = "Ubicacion"
        
    def secuencia_menu(self):
        while True:
            x = self.menu()#esta es una variable que abre nuestro menu y segun lo que escojas es lo que se va a ejecutar
            match x:#parecido al while true lo que hace es que segun el valor de x te va a escojer una opcion y la va a ejecutar
                case "1":
                    self.registrar()
                case "2":
                    self.editar()
                case "3":
                    self.eliminar()
                case "4":
                    self.consulta()
                case "5":
                    break
                case _:
                    print("Favor de escribir una opcion valida")
            
    def menu(self):#SI FUNCIONA !!NO LE MUEVAS!!
        print("_________________________________________")
        print(f"|{self.ubicacion.center(39)}|")
        print("|                                       |")
        print("|Accion a realizar a la tabla:          |")
        print("|1)Registrar                            |")
        print("|2)Editar                               |")
        print("|3)eliminar                             |")
        print("|4)consultar                            |")
        print("|5)salir                                |")
        print("_________________________________________")
        return input("¿Cual opcion deseas escojer?: ")
    
    def registrar(self):
        Zona_celda = input("Ingrese la zona de la celda: ")
        Numero = input("Ingrese el numero de celda: ")
        Ubicacion = input("Ingrese la ubicacion de la celda: ")
        query = "INSERT INTO ubicacion (Zona_Celda,Nombre,Ubicacion) Values (%s,%s,%s)"
        #aqui se va a poner los datos que estan punteados
        cursor.execute(query, (Zona_celda,Numero,Ubicacion))
        conecction.commit()
        print("se relaizo correctamente el registro...")

    def editar(self):
        self.consulta()
        id = input("ingrese el id de la zona a editar: ")
        cursor.execute("SELECT * FROM ubicacion WHERE id = %s;",(id,))
        resultado = cursor.fetchall()

        print(f"el Id de la zona es {resultado[0][0]}")
        print(f"La zona de la celda es {resultado[0][1]}")
        Zona_celda = input("Ingrese la zona de la celda: ")
        print(f"EL numero de la celda es {resultado[0][2]}")
        Numero = input("Ingrese el numero de celda: ")
        print(f"La ubicacion es {resultado[0][3]}")
        Ubicacion = input("Ingrese la ubicacion de la celda: ")
        comando = "UPDATE ubicacion SET Zona_celda=%s, Numero=%s,Ubicacion=%s WHERE id=%s"
        cursor.execute(comando, (Zona_celda,Numero,Ubicacion, id))
        conecction.commit()
        print("------------------------------------")
        print("edicion completada")

    def eliminar(self):
        ubicacion.consultar()
        id = input("ingresar el id a borrar:")
        comando = "DELETE FROM ubicacion WHERE id = %s"
        cursor.execute(comando, (id,))
        conecction.commit()
        print("se eliminada exitosamente")
        pass

    def consulta(self):
        cursor.execute("SELECT * FROM ubicacion")
        Mostrar = cursor.fetchall()
        print("---------------------------------------")
        if Mostrar:
            for fila in Mostrar:
                print(f"id de la zona {fila[0]}")
                print(f"Zona de la Zona : {fila[1]}")
                print(f"Numero de Celda {fila[2]}")
                print(f"Ubicacion de la celda {fila[3]}")
                print("--------------------------------------------------------")
        else:
            print("no hay datos disponibles")


#Menu !!!!!SI FUNCIONA NO LE MUEVAS!!!!!
preso = Preso()
celda = Celda()
crimen = Crimen()
guardias = Guardias()
libercondi = LiberCondi()
ubicacion = Ubicacion()

while True:
    print("_________________________________________")
    print("|         Organizador de tienda         |")
    print("|                                       |")
    print("|Accion a realizar a la tabla:          |")
    print("|1)Preso                                |")
    print("|2)Celda                                |")
    print("|3)Crimen                               |")
    print("|4)Guardias                             |")
    print("|5)Libertad condicional                 |")
    print("|6)Ubicacion                            |")
    print("|7)Salir                                |")
    print("_________________________________________")
    x = input("¿Cual opcion deseas escojer?")
    match x:
        case "1":
            preso.secuencia_menu()
        case "2":
            celda.secuencia_menu()
        case "3":
            crimen.secuencia_menu()
        case "4":
            guardias.secuencia_menu()
        case "5":
            libercondi.secuencia_menu()
        case "6":
            ubicacion.secuencia_menu()
        case "7":
            break
        case _:
            print("Favor de escribir una opcion valida")

#Menu !!!!!NO LE MUEVAS!!!!!