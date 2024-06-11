"""
 una funcion es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa

 sintaxis:

 def nombreMifuncion(parametros:)










"""
#1- funcion que no recibe parametro y no regresa valoe

def sumaNumeros1():
    n1=int(input("numero # 1:"))
    n2=int(input("numero # 2:"))
    suma=n1+n2
    print (f"{n1}+{n2}={suma}")

sumaNumeros1() 

#2- funcion que no recibe parametros y regresa valor
def sumaNumeros2():
    n1=int(input("numero # 1:"))
    n2=int(input("numero # 2:"))
    suma=n1+n2
    return f"{n1}+{n2}={suma}"

print(sumaNumeros2())


#3-funcion que recibe parametros y no regresa valor
def sumaNumeros3(n1,n2):
    suma=n1+n2
    print (f"{n1}+{n2}={suma}")

n1=int(input("numero # 1:"))
n2=int(input("numero # 2:"))
sumaNumeros3(n1,n2)   



#4-funcion que recibe parametros y regresa valor
def sumaNumeros4(n1,n2):
    suma=n1+n2
    return f"{n1}+{n2}={suma}"

n1=int(input("numero # 1:"))
n2=int(input("numero # 2:"))
print(sumaNumeros4(n1,n2) )


#ejemplo 6 crear un programa que solicite a traves de una funcion la siguiente informacion:
#nombre del paciente, edad, estatura, tipo de sangre, utilizar los 4 tipos de funciones.
