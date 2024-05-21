#Existe una estructura de condicion llamada "if"
#la cual evalua una condicion para encontrar el valor "True" y si se cumple
#la condicion se ejecuta la linea o lineas de codigo 

#Tienes 4 variantes del if

#1.- if simple
#2.- if compuesto
#3.- if anidado
#4.- if y elif

#Ejemplo 1 if simple

# color=input("Ingresa un color")
# if color=="rojo":
#     print("soy el color rojo")

#     #Ejemplo 2 if compuesto

# color=input("Ingresa un color")

# if color=="rojo":
#     print("soy el color rojo")
# else:
#     print("No soy el color rojo soy otra cosa")

#     #Ejemplo 3 if anidado

#     color=input("Ingresa un color")

# if color=="rojo":
#     print("soy el color rojo")
#     if color!="rojo":
#         print("No soy el color rojo")
# else:
#     print("No soy el color rojo soy otra cosa")

#      #Ejemplo 4 if y elif

#     color=input("Ingresa un color")

# if color=="rojo":
#     print("soy el color rojo")
# elif color=="amarillo":
#     print("Soy el color amarillo")

# elif color=="azul":
#     print("Soy el color azul")

# elif color=="morado":
#     print("Soy el color morado")
# else:
#     print("No soy ninguno de los anteriores")

#Ejemplo 5 Crear un programa que solicite el numero de la semana
#e imprimar en pantalla el dia que le corresponde


dia =int(input("Ingresa un numero de la semana"))

if dia== 1:
    print("lunes")

if dia== 2:
    print("martes")

if dia== 3:
    print("miercoles")

if dia== 4:
    print("jueves")

if dia== 5:
    print("viernes")

if dia== 6:
    print("sabado")

if dia== 7:
    print("domingo")

else:
    print("No soy un dia de la semana")



