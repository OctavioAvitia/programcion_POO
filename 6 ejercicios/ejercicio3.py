# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for

numero=1
while numero<=60:
     cuadrados=numero * numero
     print(f"el cuadrado {numero} es {cuadrados}")
     numero += 1

for numero in range (1,61):
     cuadrado=numero * numero
     print(f"el cuadrado de {numero} es {cuadrado}")
     
