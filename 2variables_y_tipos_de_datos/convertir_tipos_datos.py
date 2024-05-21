#Comentario de varias lineas
#Nota: A la hora de concatenar cadenas no es posible incluir en 
#algunas ocasiones contenido de variables que no sean del tipo str

#comentario de una linea

#concatenar un str con str

texto="Soy una cadena de texto"
numero=23

print(texto+" y soy otra cadena")

#concatenar un int con str

numero=23
numero_str=str(numero)

print("el numero: "+numero_str)

#para un solo paso
print("el numero: "+str(numero))

#concatenar un str con int

n1='23'
n2=33

suma=int(n1)+n2

print("el numero: "+str(suma))

#concatenar un float con str

n1='23'
n2=33.0

suma=int(n1)+n2

print("el numero: "+str(int(suma)))
print(f"el numero: {suma}")

#conectar un float y float con float

n1='23.34'
n2='33.99'

suma=float(n1)+float(n2)

print(f"el numero: {suma}")



