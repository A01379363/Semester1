#calcula distacia entre dos puntos del plano cartesiano

x1=float(input("punto inicial de x: "))
y1=float(input("punto inicial de y: "))
x2=float(input("punto final de x: "))
y2=float(input("punto final de y: "))

distancia=round((((x2-x1)**2)+((y2-y1)**2))**(1/2), 2)

print("{0:.2f}".format(distancia))
