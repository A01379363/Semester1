num_to_avg = int(input("Cuantos numeros se van a promediar? "))
i = 0
sum = 0
while i < num_to_avg:
    num = float(input("Numero: "))
    sum = sum + num
    i += 1

avg = sum/num_to_avg
print(f"El promedio es: {avg}")
