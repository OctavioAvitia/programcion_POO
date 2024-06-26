
from coches import *

print("Objeto 1")
coche1=Coches("Blanco","VW","2022",220,150,5)
# coche1.getInfo()


# print("Objeto 2")
# coche2=Coches("Azul","Nissan","2020",180,150,6)
# # coche2.setColor("Blue Demon")
# coche2.getInfo()

#Implementar el encapsulamiento o visibilidad

print(coche1.atributo_publico)
# print(coche1.__atributo_publico) #Esto no es posible
print(coche1.MetodoPublico())
# coche1.__MetodoPrivado() #Esto no es posible
coche1.getMetodoPublico()