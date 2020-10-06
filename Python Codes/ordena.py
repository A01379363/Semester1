#ordena en forma ascendente 3 numeros enteros

x=int(input())
y=int(input())
z=int(input())

if x>y>z:
    print(z)
    print(y)
    print(x)
elif x>y>z:
    print(z)
    print(y)
    print(x)
elif y>x>z:
    print(z)
    print(x)
    print(y)
elif y>z>x:
    print(x)
    print(z)
    print(y)
elif z>x>y:
    print(z)
    print(x)
    print(y)
elif z>y>x:
    print(x)
    print(y)
    print(z)
else:
    print(x)
    print(y)
    print(z)
    
