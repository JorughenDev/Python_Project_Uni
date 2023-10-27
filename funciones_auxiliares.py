import random as r
import colorama as cl
import os
cl.init(autoreset=True)

def get_ruta():
    while True:
        ruta = input(cl.Fore.LIGHTMAGENTA_EX+"Especifique la ruta donde esta el archivo:")
        if os.path.isfile(ruta):
            return ruta
        else:
            print(cl.Fore.RED+"El archivo no existe o la ruta ha sido escrita incorrectamente.")
def get_save_file_name_and_route(ruta):
    complete = False
    while not complete:
        name = input(cl.Fore.LIGHTMAGENTA_EX+"Nombre del archivo: ")
        absolute_ruta = ruta + name
        absolute_ruta = absolute_ruta.replace("//","/")
        if os.path.isfile(absolute_ruta):
            print(cl.Fore.CYAN+"Este archivo ya existe")
            print(cl.Fore.CYAN+"Desea sobreescribirlo?")
            choice = input(cl.Fore.CYAN+"si/no\n").lower()
            if choice == "si":
                return absolute_ruta
            elif choice == "no":
                complete = True
            else:
                print(cl.Fore.RED+"Valor invalido")
        else:
            return absolute_ruta

def checkNum(string: str, reveladas, dificultad, tempRevelada):
    if string.isdigit():
        num = int(string)
        if (num > 0) and (num not in reveladas) and (num <= (dificultad[2]*2)) and (num != tempRevelada):
            return True
        return False


def get_carpeta():
    ruta  = ""
    ruta_valida = False
    while not ruta_valida:
        ruta = input(cl.Fore.LIGHTMAGENTA_EX+"Donde desea guardar sus archivos: ")
        if os.path.isdir(ruta):
            ruta_valida = True
        else:
            print(cl.Fore.RED+"La ruta que ha ingresado no existe o es un archivo.")
            print(cl.Fore.RED+"Por favor ingresar una ruta a una carpeta.")
    return ruta


def valid_contra(database):
    validContra = False
    while not validContra:
        contrasena = input(cl.Fore.GREEN+"Ingrese su contrasena: ")
        if not valid_data(contrasena):
            print(cl.Fore.RED+"La contraseña debe tener como minimo un caracter, y no terminar ni empezar con espacios")
        else:
            validContra = True
            return contrasena

def valid_user(database):
    validUser = False
    while not validUser:
        usuario = input(cl.Fore.GREEN+"\nIngrese su usuario: ")
    #checkeamos si no se repite el usuario
        if check_duplicate(usuario,database):
            print(cl.Fore.RED+"Este usuario ya se encuentra registrado ingrese otro nombre")
        elif not valid_data(usuario):
            print(cl.Fore.RED+"El usuario debe tener como minimo un caracter, y no terminar ni empezar con espacios")
        else:
            validUser = True
            return usuario

def empate(jugadores_cartas):
    empate = True
    cartas_en_orden = []
    while empate:
        cartas_en_orden = sorted(list(jugadores_cartas.values()), reverse=True) # asi podemos ver si hay duplicado al transofmralo en lista
        if check_duplicate_cards(cartas_en_orden):  # es verdad cuando hay duplicados
            jugadores_cartas = shuffle(jugadores_cartas)
        else:
            empate = False
    return cartas_en_orden

def login(size, database):
    jugadores_cartas = {}
    valid_users = []
    for numero_jugador in range(size) :
        print(cl.Fore.LIGHTMAGENTA_EX+"\nJUGADOR " + str(numero_jugador+1))
        usuario = input(cl.Fore.CYAN+"\nIngrese su usuario: ")
        validUser = False
        while not validUser:
            while usuario not in database.keys():         # verifica si el usuario esta registrado
                usuario = input(cl.Fore.RED+"Usuario Incorrecto\n"+ cl.Fore.CYAN+"Ingrese su usuario: ")
            #     verifica si el usuario no esta repetido con el de antes
            if same_user(valid_users,usuario):
                usuario = input(cl.Fore.RED+"Usuario repetido\n"+ cl.Fore.CYAN+"Ingrese su usuario: ")
            else:
                validUser = True
        contrasenia = input(cl.Fore.CYAN+"Ingrese su contrasena: ")
        while contrasenia != database[usuario]:
            contrasenia = input(cl.Fore.RED+"Contraseña Incorrecta!!!\n" + cl.Fore.CYAN+"Ingrese su contrasena: ")
        carta = r.randint(1, 13) #IMPORTANTE PARA SACAR CARTA DE JUGADOR
        jugadores_cartas[usuario] = carta
        valid_users.append(usuario)
    return jugadores_cartas

def check_player_size(database):
    invalidaCantidadJugadores = True
    while invalidaCantidadJugadores:
        cantidadJugadores = input(cl.Fore.CYAN+"Seleccione la cantidad de jugadores entre 2 y 4: ")
        if cantidadJugadores.isnumeric():
            if int(cantidadJugadores) > len(database):
                if int(cantidadJugadores) <= 4:
                    print(cl.Fore.RED+"No hay esa cantidad de jugadores registrados!! ")
            elif int(cantidadJugadores) < 2:
                print(cl.Fore.RED+"El juego requiere de 2 jugadores!!!")
            else:
                invalidaCantidadJugadores = False
                return int(cantidadJugadores)
#"♠","♡","♣","♢"
def check_difficult():
    dificultadInvalida = True
    while dificultadInvalida:
        print(cl.Fore.BLUE+"Seleccione su Dificultad:\n1. Facil\n 2. Normal \n 3. Dificil")
        dificultad = input(cl.Fore.LIGHTMAGENTA_EX+"Opcion deseada: ")
        if dificultad.isnumeric():
            if dificultad == "1" or dificultad == "2" or dificultad == "3":
                dificultadInvalida = False
                return get_difficulty(dificultad)
            else:
                print(cl.Fore.RED+"Por favor escoja una de las opciones brindadas")
        else:
            print(cl.Fore.RED+"Opcion Invalida\nPor favor seleccione nuevamente:")

def same_user(valid_users, user):
    for u in valid_users:
        if user == u:
            return True
def get_difficulty(d):
    if d == "1":
        return [4, 4, 8]
    elif d == "2":
        return [4, 8, 16]
    elif d == "3":
        return [4, 13, 26]

def valid_number(data,database):
    if data.isnumeric():
        if int(data) > len(database):
            print(cl.Fore.RED+"No hay esas cantidad de jugadores registrados!! ")
        elif int(data) < 2:
            print(cl.Fore.RED+"El juego requiere de 2 jugadores!!!")
    return True

def valid_data(data):
    if len(data) == 0 or data[0] == " " or data[-1] == " ":
        return False
    return True

def shuffle(jugadores_turnos):
    for user in list(jugadores_turnos.keys()):
        jugadores_turnos[user] = r.randint(1,13)
    return jugadores_turnos

def check_duplicate(u, database):
    for user in database.keys():
        if u == user:
            return True

def check_players(user, usuariosContrasenas):
    for usuario, contra in usuariosContrasenas.items():
        if user == usuario:
        # return "Datos Incorrectos. Ingrese los Datos nuevamentes"
            return False
        elif not usuariosContrasenas[user] == contra:
        # return "Datos Incorrectos. Ingrese los Datos nuevamentes"
            return False
    return True


def check_duplicate_cards(l):
    list_size = len(l)
    set_size = len(set(l))
    if list_size != set_size:
        return True
    return False


def create_list_turns(t):
    JugadoresEnTurnos = []
    for i in t:
        JugadoresEnTurnos.append(get_user(i))
    return JugadoresEnTurnos


def get_user(k,jugadores_turnos):
    for user, card in jugadores_turnos.items():
        if card == k:
            return user

def AJQKRTRANSFORM(numero):
    if numero == 1:
        return "A"
    elif numero == 11:
        return "J"
    elif numero == 12:
        return "Q"
    elif numero == 13:
        return "K"
    else:
        return numero

#
# usuariosContrasenas = {"karim": "gingam123", "hector": "flauta123", "pepe": "etesech", "a": "b", "b": "c", "c": "d"}
#
# JugadoresValidos = 0
#
# jugadoresTurnos = {}
#
# jugadores = 3
#
# while True:
#     for i in range(jugadores):
#         user = input()
#         password = input()
#         if check_players(user, password):
#             carta = r.randint(1, 5)
#             jugadoresTurnos[user] = carta
#         else:
#             i -= 1
#             print("Usuario o contraseña incorrectos. Por favor intentar de nuevo")
#             continue
#     turnos = sorted(list(jugadoresTurnos.values()), reverse=True)
#     if not check_duplicate_cards(turnos):
#         break
