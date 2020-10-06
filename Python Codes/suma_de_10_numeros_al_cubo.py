input_list = input("Escribe hasta 10 numeros separados por una coma: ")
if len(input_list)<=19:
    num_list = input_list.split(",")
    sum = 0
    for num in num_list:
        cubic_num = int(num)**3
        sum += cubic_num

    print(f"La suma de todos los numeros al cubo es {sum}")

else:
    print("Error: Escribiste mas de 10 numeros")