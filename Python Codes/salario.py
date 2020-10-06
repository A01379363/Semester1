#calcula el salario semanal de un trabajador

pagoHora = float(input('Pago por hora: '))
horas = float(input('Cuantas horas trabajaste esta semana? '))

salario=pagoHora*horas

if 50>=horas>=41:
    salario=pagoHora*40
    salario_doble=(((horas-40)*pagoHora)*2)
    print('$',salario+salario_doble)

elif 60>=horas>=51:
    salario=pagoHora*40
    salario_triple=(((horas-40)*pagoHora)*3)
    print('$',salario+salario_triple)

elif horas>60:
    salario=(pagoHora*40)+2000
    print('$',salario)

else:
    print('$',salario)
