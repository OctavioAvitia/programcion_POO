# Hacer un programa que muestre todos los numeros
# impares entre 2 numeros que decida el usuario

i= int(input("Ingresa el primer número: "))
f = int(input("Ingresa el segundo número: "))

if i> f:
    i, f= f, i

    print(f"Los números impares entre {i} y {f} son:")
for num in range(i, f + 1):
    if num / 2 != 0:
        print(num)