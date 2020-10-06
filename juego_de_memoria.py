# Enrique Mondelli
# Jorge Cabiedes
# Mateo Gonzalez Cosio
# Carlos Daniel Lopez
import random

lista = []
matriz = []
turno = 1
counter = 0
puntos1 = 0
puntos2 = 0
tablero = [list('-'*6) for i in range(6)]  # crea una lista que contiene 6 renglones y 6 columnas de '-'


def valores_tablero():

    for i in range(1, 19):  # agrega los numeros entre el 1 y el 18 en la lista dos veces
        lista.append(i)
        lista.append(i)

    random.shuffle(lista)  # mezcla los numeros en la lista

    j = 0
    for i in range(6):  # agrega una lista de 6 numeros a la matriz
        matriz.append(lista[0 + j:6 + j])
        j += 6


def fturno():  # funcion para imprimir a que jugador le toca escoger
    if turno == 1:
        print('\nTurno del jugador 1')

    if turno == 2:
        print('\nTurno del jugador 2')


def escoge():  # funcion para que el jugador escoja las dos casillas que quiere voltear
    global y1, x1, y2, x2
    y1 = int(input('renglon de la casilla 1: '))
    x1 = int(input('columna de la casilla 1: '))

    y2 = int(input('renglon de la casilla 2: '))
    x2 = int(input('columna de la casilla 2: '))


def print_tablero():  # funcion para imprimir la tabla
    print('   0   1   2   3   4   5')
    for i in range(6):
        if i > 0:
            print()
        print(f'{i}  ', end='')
        for j in range(6):
            if len(str(tablero[i][j])) == 1:
                print(f'{tablero[i][j]}   ', end='')
            elif len(str(tablero[i][j])) == 2:
                print(f'{tablero[i][j]}  ', end='')


valores_tablero()
print_tablero()

while counter < 18: # un while loop que acaba cuando el contador de pares sea mayor a 18
    fturno()
    escoge()
    while True:  # un while loop para los errores que puede cometer el jugador
        if y1 > 5 or x1 > 5 or y2 > 5 or x2 > 5:  # si el juagor escoge una casilla fuera del rango, intenta denuevo
            print('Fuera del rango. Intente denuevo.')
            escoge()
        elif y1 == y2 and x1 == x2:  # si el jugador escribe los mismos valores 2 veces, intenta denuevo
            print('Escogiste la misma casilla dos veces. Intente denuevo.')
            escoge()
        elif tablero[y1][x1] == matriz[y1][x1] or tablero[y2][x2] == matriz[y2][x2]:  # si el jugador escoge una casilla
            print('Esa casilla ya esta destapada. Intente denuevo.')                  # que ya este destapada,
            escoge()                                                                  # intenta denuevo
        else:  # si el jugador ya no comitio errores el loop se rompe y el juego continua
            break

    tablero[y1][x1] = matriz[y1][x1]  # reemplaza los '-' del tablero por numeros en la matriz
    tablero[y2][x2] = matriz[y2][x2]  # como si estuvieran volteando las cartas
    print_tablero()

    if matriz[y1][x1] == matriz[y2][x2]:  # si las dos casillas que escogio el jugador son igual
        print('\nCorrecto!')
        if turno == 2:  # si estaba en el turno de jugador 2 se le agrega un punto y el turno se pasa al jugador 1
            puntos2 += 1
            turno = 1
        else:  # si estaba en el turno de jugador 1 se le agrega un punto y el turno se pasa al jugador 2
            puntos1 += 1
            turno = 2
        counter += 1  # un contador para saber cuantos pares ya estan desvolteados

    else:  # si las casillas no son iguales
        print('\nIncorrecto!')
        tablero[y1][x1] = '-'  # desvoltea las cartas
        tablero[y2][x2] = '-'
        if turno == 2:  # si estaba en el turno de jugador 2 el turno se pasa al jugador 1
            turno = 1
        else: # # si estaba en el turno de jugador 1 el turno se pasa al jugador 2
            turno = 2

    seguir = input('\nDeseas seguir jugando (s/n)? ')  # pregunta al jugador si quiere seguir jugando
    if seguir == 'n':  # si el jugador responde 'n' (no), el juego acaba
        break
    print_tablero()  # imprime el tablero

print(f'El jugador 1 tuvo {puntos1} puntos.')
print(f'El jugador 2 tuvo {puntos2} puntos.')
if puntos1 > puntos2:  # si el juagor 1 tiene mas puntos que el juagor 2, gana el jugador 1
    print('El jugador 1 gano!')
elif puntos1 == puntos2:  # si los dos tienen la misma cantidad de puntos, empatan
    print('Empate!')
else:  # si el juagor 2 tiene mas puntos que el juagor 1, gana el jugador 2
    print('El jugador 2 gano!')