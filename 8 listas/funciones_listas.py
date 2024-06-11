paises=["Mexico","Usa","Brasil","China"]
numeros=[100,80,3.1416,75]
varios=["UTD",True,100,0.100]

#ordenar las listas
print(paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort()
print(numeros)

#agregar alementos
print(numeros)
numeros.append(100)
print(numeros)
numeros.insert(len(numeros),200)
print(numeros)

#remover elementos
print(numeros)
numeros.remove()
print(numeros)
numeros.pop(2)
print(numeros)

#dar la vuelta a los elemtos de una lista

print(varios)
varios.reserve()
print(varios)

#buscar un valor dentro de una lista

encontro="basil" in paises
print(encontro)
 

 #vasiar una lista o borrar
print(paises)
paises.clear()
print(paises)

#unir listas

print(varios)
varios.exted(numeros)
print(varios)

