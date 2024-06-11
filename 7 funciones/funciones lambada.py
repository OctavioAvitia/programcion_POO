#Funciones Lambda son funciones anonimas ya que sirven para abreviar funciones normales 
#y normalmente se usan para ejecutar una sola accion

"""
sintaxis:
lambda argumentos: expresion

Funciones lambda se pueden convertir en funciones normales pero NO viceversa
"""
#Ejemplo 1
def suma(n1,n2):
    return n1 + n2
print(suma(4,2))

suma = lambda n1, n2: n1 + n2
print(suma(4,3))


#ejemplo 2

elevar = lambda num: num * num
print(elevar(4))

#ejemplo 3
def mensaje():
    nombre = input("Ingrese su nombre")
    return f"Hola, {nombre}! Eres increible"
print(mensaje())

mensaje = lambda: f"Hola,{input("Ingresa tu nombre")}! Eres Increible"
print(mensaje())