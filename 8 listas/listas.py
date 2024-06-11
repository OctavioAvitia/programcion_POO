"""
 list (array)
 son colecciones o conjunto de datos/valores bajo
 un mismo nomnre, para acceder a los valores se 
 hace con un indice numerico

 nota:sus valores si son modificables

 la lista es una coleccion ordenada y modificable. permite miembros


 """


#ejemplo 1 crear una lista con valores numericos enteros e imprimir la lista

numeros=[23,34]
print(numeros)

#recorrer la lista con un for

for i in numeros:
    print(i)

#recorrer la lista con un while
i=0
while i<len(numeros):
    print(numeros[i])
    i+=1

#ejemplo 2 crear una lista de palabras posteriormente
# ingresar una palabra para buscar la coincidencia em listas 
#. e indicar si aparece la palabra y en que posicion en caso 
#contrario indicar una solaves si no la encontro

palabra=["hola","2024","10.23","true"]

palabra_buscar=input("ingresa la palabra a buscar: ")
















#ejemplo 3 lista multilinea o multidimencional (matriz) para crear una agenda telefonica

agenda=[
    ["carlos",6181234567],
    ["fernando",6182334567],
    ["matias",6691112233],
    ["juan polainas",6182332345]
]

print(agenda)

for i in agenda:
    print(f"{agenda.index(i)+1}.-{i}")


    #ejemplo 4 crear un programa que permita gestionar (administrar) peliculas, colocar un menu de 
    #opciones para agregar, remover, consultar peliculas.
    #notas.
    #1.- utilizar funciones y mandar llamar desde otro archivo
    #2.- utilizar listas para almacenar los nombres de peliculas

def InsertarPeliculas():
    peliculas=input("ingrese la pelicula: ")
    peliculas.uppend(peliculas)
    espereTecla()

def eliminarPeliculas():
    pelicula=input("ingrese la pelicula: ")
    peliculas.remover(pelicula)
    espereTecla()   

peliculas=[]

print("\n\t..:::jordis:::..\n 1.- Agregar  \n 2.-Eliminar \n 3.-Consultar \n 4.-SALIR")
opcion=input("\t elije una opcion:").upper()


if opcion=="1" or opcion=="AGREGAR":
    InsertarPeliculas()
elif opcion=="2" or opcion=="ELIMINAR":
    eliminarPeliculas()
 
    