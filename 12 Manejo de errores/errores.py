#manejo de errores es la forma en la que tienen los lenguajes de programacion 
#para evitar que sucede errores en tiempo de ejecucion
#..::vuleerror:invalid literal for int() with base 10::..
#ejemplom 1 error cuando una variable no se genera

try:
    nombre=input("dame el nombre: ")

    if len(nombre)>1:
     nombre_usuario="el nombre es: "+nombre

    print(nombre_usuario)    
except:
  print("es necesario introducir un nombre de usuario...")

  #ejemplo 2 cuando se solicita un numero y se introduce una letra

  

try:
   numero=int(input("dame un numero:"))

   if numero>0:
    print("soy un numero entero positivo")
   else:
    print("soy un numero entero negativo")
except:
    print("no se puede covertir un caracter no numerioco a numero")
else:
  print("todo se ejecuto sin errores")

#ejemplo 3 cuando se generan multiples excepciones
      
try:
  numero=int(input("name un numero: "))

  print("el cuadrado es: "+str(numero*numero))
except ValueError:
   print("debes de introducir un numero no se puede convertir un caracter que sea numerico")
except TypeError:
   print("no es posible covertir el numero a entero")
else: 
  print("finalizo correctanmente")
finally:
  print("listo se termino") 
       
  


