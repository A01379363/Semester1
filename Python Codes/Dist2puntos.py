#clacula distancia entre dos puntos
import math

x1 = int(input("x1: "))
x2 = int(input("x2: "))
y1 = int(input("y1: "))
y2 = int(input("y2: "))

dist = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

print("La distancia es igual a ",dist)
