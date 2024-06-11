# Hacer un programa que resuelva lo siguiente.
# ¿Cuanto es el X por ciento de X numero?

numero = float(input("Ingresa el número:"))
porcentaje = float(input("Ingresa el porcentaje (sin porcentaje):"))

resultado = (porcentaje / 100) * numero

print(f"El {porcentaje}% de {numero} es: {resultado}")