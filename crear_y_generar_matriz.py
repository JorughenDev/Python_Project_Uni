import random
import colorama as cl
from colorama import init, Fore
init()

# el nnumero de cartas por matriz dependiendo de la dificultad
"""
    SOLO DEBEN MANDARSE ESTOS VALORES
    Facil (8)
    Normal (16)
    Dificl (26)
"""

palosCarts = [cl.Fore.BLACK+"♠",cl.Fore.BLACK+"♣",cl.Fore.RED+"♡",cl.Fore.RED+"♢"]

def crearCartas(dificultad: int):
    # funcion que retorna cartas aleatorias, anidada para que sea mas facil importar crearCartas() a otros scripts
    def crearCarta():
        palosCarts = ["♠", "♡", "♣", "♢"]
        carta = random.randint(1, 13)
        palo = random.choice(palosCarts)

        # asigna cartas especiales
        if carta == 1: carta = "A" + palo
        elif carta == 11: carta = "J" + palo
        elif carta == 12: carta = "Q" + palo
        elif carta == 13: carta = "K" + palo
        else: carta = str(carta) + palo

        return carta

    # generamos las cartas diferentes una de otra acorde a la dificutlad, se eliminan de la baraja original para que no se repitan, se duplican las listas para generar los pares
    cartasRandom = []
    for i in range(dificultad):
        insertda = False
        while not insertda:
            carta = crearCarta()
            if carta not in cartasRandom:
                cartasRandom.append(carta)
                insertda = True
    cartasRandom += cartasRandom

    # desordena las cartas duplicadas anteriormente
    j = 1
    for x in range(len(cartasRandom) - 1):
        temp = cartasRandom
        indiceRandom = random.randint(0, (len(cartasRandom) - 1))
        cartasRandom.append(temp.pop(indiceRandom))
        j += 1

    i = 0
    for x in cartasRandom:
        temp = x
        cartasRandom[i] = [i + 1, temp, False]
        i += 1

    return cartasRandom


"""
    SOLO DEBEN MANDARSE ESTOS VALORES
    Facil (matriz,4)
    Normal (matriz,8)
    Dificl (matriz,13)
"""


def formatoMatriz(matriz, columnas):
    listaFinal = [[] for x in range(4)]
    i = 0
    for x in range(4):
        for y in range(columnas):
            listaFinal[x].append(matriz[i])
            i += 1

    for i in range(4):
        temp = []
        for j in range(columnas):
            if listaFinal[i][j][2]:
                temp.append(str(listaFinal[i][j][1]))
            else:
                temp.append(str(listaFinal[i][j][0]))
        for k in temp:
            if "♡" in k or "♢" in k:
                print(Fore.RED + "[  " + k + "  ]", end=" ")
            elif "♣" in k or "♠" in k:
                print(Fore.BLACK + "[  " + k + "  ]", end=" ")
            else:
                print(Fore.BLUE + Fore.CYAN + "[  " + k + "  ]", end=" ")
        print("")


"""
    matriz = crearCartas(dificultad)
    usar formatoMatriz(matriz, dificultad)
"""
