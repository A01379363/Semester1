#calcula cuantos litros de pintura son necesarios para cubrir una superficie
import math

area=float(input("area (m^2) = "))
litro=float(input("cuantos metros cuadrados se pueden cubrir con un litro de pintura? "))

litros_exactos=area/litro

litros_completos=math.ceil(litros_exactos)

print(litros_completos)
