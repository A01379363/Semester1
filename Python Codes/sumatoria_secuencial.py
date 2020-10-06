numero = int(input())
suma = 0
lista = []
sumaTotal = 0

for i in range(1, numero + 1):
    suma += i
    lista.append(i)
    print(*lista, sep="+", end=" = ")
    print(suma)
    sumaTotal += suma

print("La suma de la serie hasta el número " + str(numero) + " es: " + str(sumaTotal))