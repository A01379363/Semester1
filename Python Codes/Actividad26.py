lista = []
sum = 0
sum2 = 0

while True:
    num = input()
    if num == '/':
        break
    lista.append(int(num))
for i in range(len(lista)):
    num2 = input()
    if num2 == '/':
        break
    lista[i] += int(num2)

while True:
    user_input = input()
    if user_input == '*':
        break

print(lista)

