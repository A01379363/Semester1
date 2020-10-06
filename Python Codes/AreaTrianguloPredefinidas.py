#calcula el area de un triangulo con funciones predefinidas
import math

a=float(input("a = "))
b=float(input("b = "))
c=float(input("c = "))

s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))


print("El area es igual a",area)
