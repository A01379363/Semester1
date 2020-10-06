#calcula el discriminante
import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discriminante = pow(b, 2) - 4 * a * c

print("El discriminante es igual a ",discriminante)

#calcula x1 y x2

x1 = (-b + math.sqrt(discriminante)/(2 * a))
x2 = (-b - math.sqrt(discriminante)/(2 * a))

print("x1 =",x1)
print("x2 =",x2)
