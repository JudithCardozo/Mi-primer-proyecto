"""
   Ejemplo de diagrama de flujo
                                 """
print("Inicio")

a = 3
b = 7
s = a + b

print(s)
print("Fin")

#Tipos de datos

#int(Enteros)======= 1,2,5000000...
#float(Decimales)=== 1.23,5.7,3.7...
#string(caracteres)= "spam"
#Bool=============== True(1) o False (0)

#Libreria Math
#nos ayuda al calculo de distintas funciones matematicas: logaritmica, trigonometrica, etc.
#para usarla es necesario importarla a traves del codigo import.

#Operaciones matematicas

x1 = 5
x2 = 2

print("calculando las operaciones basicas")

suma = x1 + x2

print("la suma es:", suma)

resta = x1 - x2

print("la resta es:", resta)

multi = x1 * x2

print("la multiplicacion es:", multi)

print("todos los tipos de divisiones")

div1 = x1 % x2
print("el residuo de la division es:", div1)

div2 = x1 // x2
print("el cociente de la division es:", div2)

div3 = x1 / x2
print("la division es:", div3)

ae = 5
ae += 2
print(ae)

import math


ru = 16
mm = math.sqrt(ru)
print(mm)

import math


h = math.hypot(3,4)
print(h)