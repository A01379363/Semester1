#determina si un triangulo es equilatero, isósceles o escaleno

x=int(input("X = "))
y=int(input("Y = "))
z=int(input("Z = "))

if (x+y>z and x+z>y and y+z>x):
        if x==y==z:
            print("EQUILATERO")
        elif (x==y) or (y==z) or (x==z):
            print("ISOSCELES")
        else:
            print("ESCALENO")
else:
    print("NO ES TRIANGULO")
