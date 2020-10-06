number1 = int(input())
number2 = int(input())
if number1==number2:
    print("No hay pares")

if number1>number2:
   number1, number2 = number2, number1

for num in range(number1, number2):
    if num%2 == 0:
        print(num)
    else:
        print("No hay pares")