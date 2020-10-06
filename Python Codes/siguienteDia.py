#devuelve la fecha del dia siguiente

fecha_año = int(input())
fecha_mes = int(input())
fecha_dia = int(input())

if fecha_mes==(4,6,9,11) and fecha_dia==30:
    fecha_mes += 1
    fecha_dia = 1 

elif fecha_mes==(1,3,5,7,8,10,12) and fecha_dia==31:
    fecha_mes += 1
    fecha_dia = 1

elif fecha_mes==12 and fecha_dia==31:
    fecha_año += 1
    fecha_mes = 1
    fecha_dia = 1

elif (fecha_año%4)!=0 and fecha_mes==2 and fecha_dia==28:
    fecha_mes += 1
    fecha_dia = 1

elif (fecha_año%4)==0 and fecha_mes==2 and fecha_dia==29:
    fecha_año
    fecha_mes += 1
    fecha_dia = 1

else:
    fecha_dia += 1

print(fecha_año)
print(fecha_mes)
print(fecha_dia)
