lista_temp = [5.5, 12.48, 31.54, 20.45, 17.7, 28.3, 35.4]

max1 = lista_temp[0]
min1 = lista_temp[0]
sum = 0
for temp in lista_temp:
    if temp > max1:
        max1 = temp
    if temp < min1:
        min1 = temp

    sum += temp

promedio = sum/len(lista_temp)
print('Promedio de Temperaturas:', promedio)
print('Tempreatura maxima:', max1)
print('Temperatura minima:', min1)

lista_temp.sort()

print('Lista ordenada:', lista_temp)

