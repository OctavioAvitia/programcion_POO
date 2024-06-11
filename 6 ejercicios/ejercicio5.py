#Hacer un programa que muestre todos los numeros
# entre 2 numeros que diga el usuario

p=int(input("primer numero:"))
f=int(input("segundo numero:"))

print("los numero entre" , p, "y" , f, "son")

for numero in range (p+1,f):

    print(numero)

