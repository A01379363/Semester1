#idica si un punto esta sobre, dentro o fuera de una circunferencia
import math

radius = int(input())
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

distance = math.sqrt((x2-x1)**2+(y2-y1)**2)

if distance < radius:
    print('DENTRO')

elif distance > radius:
    print('FUERA')

elif distance == radius:
    print('SOBRE')

