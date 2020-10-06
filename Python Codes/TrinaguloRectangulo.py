#resuelve un triangulo rectangulo
import math

co=int(input("Cateto opuesto = "))
angulo=int(input("Angulo = "))

radianes=math.radians(angulo)

ca=co/math.tan(radianes)

print("El Cateto adyacente es igual a",ca)

hip=co/math.sin(radianes)

print("La hipotenusa es igual a",hip)


