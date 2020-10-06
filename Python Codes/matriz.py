matriz = [[3, 5, 7, 8, 9],
          [1, 2, 4, 7, 6],
          [10, 11, 12, 13, 14],
          [-1, 2, 4, -3, 0],
          [-3, 2, 9, 4, 1]]

for i in range(len(matriz)):
    matriz[i][i] = 1
    for j in range(5):
        if j > i:
            matriz[i][j] = 0

print(matriz)
