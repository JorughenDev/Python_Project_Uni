from crear_y_generar_matriz import *
import colorama as cl
cl.init(autoreset=True)
from funciones_auxiliares import checkNum

"""
    if d == "1":
        return [4, 4, 8]
    elif d == "2":
        return [4, 8, 16]
    elif d == "3":
        return [4, 13, 26]
"""

def juegazo(Dificultad, jugadoresOrdenados):
    # infocartas es la lista de cartas aleatorias con los datos [nCarta, cartaSimbolo, True/False]
    infoCartas = crearCartas(Dificultad[2])
    formatoMatriz(infoCartas, Dificultad[1])
    contador = len(infoCartas)
    reveladas = []

    # Puntaje
    jugadoresFinal = [[x, 0] for x in jugadoresOrdenados]
    #El juego
    while contador > 0:
        for player in jugadoresFinal:
            if contador <= 0:
                break
            tempRevelada = 0
            
            print(f"--------Turno de {player[0]}--------")
        #FORMATO DE UNA CARTA [..., [n, carta, Bool], ...]
            
        #elegir 2 cartas y validar si ya han sido elegidas o no son numeros de cartas permitidas
            choice1, choice2 = 0, 0
            validCard1, validCard2 = False, False
            while not validCard1: 
                choice1 = input(Fore.WHITE + "Elija una carta no revelada: ")
                validCard1 = checkNum(choice1, reveladas, Dificultad, tempRevelada)
            choice1 = int(choice1)
            
            tempRevelada = choice1
            
            while not validCard2: 
                choice2 = input(Fore.WHITE + "Elija otra carta no revelada: ")
                validCard2 = checkNum(choice2, reveladas, Dificultad, tempRevelada)
            choice2 = int(choice2)
            
        #imprimir la matriz con las cartas reveladas
            infoCartas[choice1-1][2] = True
            infoCartas[choice2-1][2] = True
            formatoMatriz(infoCartas, Dificultad[1])
            
        #Si las cartas son iguales las deja descubiertas (bool True), si no, cubiertas (bool False). 
        #Si son iguales, le da un punto al jugador
            if infoCartas[choice1-1][1] != infoCartas[choice2-1][1]:
                print(cl.Fore.RED + " ◄ Las cartas no son iguales ► ")
                infoCartas[choice1-1][2] = False
                infoCartas[choice2-1][2] = False
                formatoMatriz(infoCartas, Dificultad[1])
            elif infoCartas[choice1-1][1] == infoCartas[choice2-1][1]:
                print(cl.Fore.GREEN + "Las cartas son iguales ☻ ")
                player[1] +=1
                formatoMatriz(infoCartas, Dificultad[1])
                contador -= 2
                reveladas.append(choice1)
                reveladas.append(choice2)
                
        #Imprimir puntaje
            print(cl.Fore.LIGHTYELLOW_EX +" • Puntaje • ")
            for player in jugadoresFinal:
                print(cl.Fore.GREEN + str(player), end="")
            print("")
    ganador = ""
    puntajemayoir = 0
    for player_data in jugadoresFinal:
        if player_data[1] == puntajemayoir:
            ganador = "Hay empate"
        if player_data[1] > puntajemayoir:
            ganador = player_data[0]
            puntajemayoir = player_data[1]
    if ganador == "Hay empate":
        print(cl.Fore.LIGHTYELLOW_EX+"Hay empate!!!")
    else:
        print(cl.Fore.LIGHTYELLOW_EX+"El ganador es " + ganador + " con " + str(puntajemayoir) + " puntos!!!")
    """
        AQUI VA LA ESTRUCTURE QUE PRINTEA AL GANADOR
    """
        
        
        



    
    