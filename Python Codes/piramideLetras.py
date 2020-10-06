alphabet = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = int(input())
if num < 1 or num > 26:
    print("Error: Solo se aceptan numeros mayor a 0 y menor a 27")
else:
    for i in range(1, num+1):
        for j in range(num - i):
            print(' ', end=' ')
        for j in range(1, i):
            print(alphabet[j], end=' ')
        for i in range(i, 0, -1):
            print(alphabet[i], end=' ')

        print('\n')
