i = 2
toggle = 0
num = int(input('Numero: '))

while i<num:
    if (num%i) == 0:
        toggle = 1
        print(f'{num} no es un numero primo')

    i += 1

if toggle == 0:
    print(f'{num} es un numero primo')