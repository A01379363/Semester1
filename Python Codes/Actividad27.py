def determinante():
    matriz = []

    numstr1 = input()
    nums = numstr1.split()
    matriz.append(nums)

    numstr2 = input()
    nums2 = numstr2.split()
    matriz.append(nums2)

    if len(nums) > 2 < len(nums2):
        print('la matriz no es cuadrada')

    elif len(nums) > len(nums2) or len(nums) < len(nums2):
        print('La matriz tiene un tamaño diferente a 2')

    else:
        det = (int(matriz[0][0])*int(matriz[1][1]))-(int(matriz[1][0])*int(matriz[0][1]))
        print(det)


determinante()
