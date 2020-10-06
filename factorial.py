
while True:
    num = int(input("Numero: "))
    factorial = 1
    while num>1:
        factorial = factorial*num
        num = num-1

    print(f"El factorial es {factorial}")
    salir = input("Salir? ")
    if salir == "si":
        break
