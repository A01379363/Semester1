i = 1
mayor = 0
while i <= 15:
    num = int(input('Numero: '))
    if num > mayor:
        mayor = num
    i += 1


print(f'El mayor es: {mayor}')