def tiempo_a_segundos():
    horas = int(input('Horas: '))
    minutos = int(input('Minutos: '))
    segundos = int(input('Segundos: '))
    
    horas_en_segundos = horas*3600
    minutos_en_segundos = minutos*60
    total_segundos = segundos + horas_en_segundos + minutos_en_segundos
    print(f'El proceso tardo {total_segundos} segundos en total')

print('Cuanto tardo el primer proceso?')
tiempo_a_segundos()

print('Cuanto tardo el segundo proceso?')
tiempo_a_segundos()

