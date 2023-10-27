import random
#Iniciar_juego_de_memoria DEPRECATED
from crear_y_generar_matriz import *
from funciones_auxiliares import *
import colorama as cl
from juegazoo import juegazo
import os

usuariosContrasenias = {}
jugadoresOrdenados = []
Dificultad = 0
Opcion = -1

# jugadoresTurnos = {}
# jugadoresOrdenados = []

def registrarUsuario(database):
    # validUser = False
    usuario = valid_user(database)
    contrasena = valid_contra(database)
    database[usuario] = contrasena
    print(cl.Fore.CYAN+"\nUsuario '" + usuario + "' creado exitosamente.\n")
    return database


def EstablecerTurnos(database):
    dificultad = check_difficult()

    cantidadJugadores = check_player_size(database)
    #bucle para que los jugadores se logen

    jugadores_cartas = login(cantidadJugadores,database)

    cartas_en_orden = empate(jugadores_cartas)

    orden_user = []

    for carta in cartas_en_orden:
        orden_user.append(get_user(carta,jugadores_cartas))

    for user in orden_user:
        print(cl.Fore.YELLOW+"\nCarta para " + user + " " + str(AJQKRTRANSFORM(jugadores_cartas[user])) + random.choice(palosCarts)+cl.Fore.BLUE)
    #el simbolo de la carta no afecta en nada si lo que compararemos al final es si una carta es mayor que la otra
    # solo se dejara para crear la ilusion de sacar una carta aleatoria
    print("")
    for i in range(0,cantidadJugadores):
        print(cl.Fore.CYAN+"Turno " + str(i+1)  + ": " + orden_user[i])

    print("")

    return dificultad, orden_user

def save_players(database):
    ruta = get_carpeta()
    absolute_ruta = get_save_file_name_and_route(ruta)
    if absolute_ruta == None:
        return None
    save_file = open(r'{}'.format(absolute_ruta),"w")
    datos = str(database)
    print(cl.Fore.LIGHTMAGENTA_EX+str(len(database))+ " jugadores: ")
    for user in database.keys():
        print(cl.Fore.CYAN+user)
    choice = input(cl.Fore.LIGHTMAGENTA_EX+"Desea guardar este archivo?\n"+cl.Fore.CYAN+"si/no\n").lower()
    if choice == "si":
        save_file.write(datos)
        print(cl.Fore.LIGHTYELLOW_EX+"Archivo guardado exitosamente.")
    # datos = datos.replace("}{",",")
    # print(datos)

def load_players(ruta,database):
    save_files = open(ruta, "r")
    save_files = eval(save_files.read())
    print(cl.Fore.MAGENTA + str(len(save_files))+ " jugadores: ")
    for user in save_files.keys():
        print(cl.Fore.CYAN + user)
    choice = input(cl.Fore.LIGHTMAGENTA_EX+"Desea cargar este archivo? \n"+cl.Fore.CYAN+"si/no\n").lower()
    if choice == "si":
        return save_files
    else:
        return database

print(cl.Fore.LIGHTMAGENTA_EX+"−−−−−−− BIENVENIDO AL JUEGO DE MEMORIA −−−−−−−")

while Opcion != "0":
    print(cl.Fore.LIGHTMAGENTA_EX+"Seleccione una de las siguientes opciones:\n"+cl.Fore.CYAN+"1. Registrar al Jugador\n2. Establecer turno\n3. Iniciar Juego de Memoria\n4. Guardar jugadores\n5. Cargar jugadores\n0. Salir")
    Opcion = input(cl.Fore.LIGHTMAGENTA_EX+"\nOpcion deseada: ")
    if Opcion == "1":
        usuariosContrasenias = registrarUsuario(usuariosContrasenias)
    elif Opcion == "2":
        # minimo 2 usuarios
        if 2 <= len(usuariosContrasenias):
            Dificultad, jugadoresOrdenados = EstablecerTurnos(usuariosContrasenias)
        else:
            print(cl.Fore.RED+"\nDeben registrarse 2 jugadores como minimo!!!\n")

    elif Opcion == "3":
        #minimo 2 usuarios registrados y con turnos establecidos
        if 2 <= len(usuariosContrasenias) and 2<=len(jugadoresOrdenados):
            jugadoresPuntaje = [0, 0, 0, 0]
            #hola va aqui el juego.
            juegazo(Dificultad,jugadoresOrdenados)
        else:
            print(cl.Fore.RED+"\nDeben registrarse 2 jugadores como minimo y seleccionar turnos!!!\n")

    elif Opcion == "4":
        if 1<=len(usuariosContrasenias):
            save_players(usuariosContrasenias)
        else:
            print(cl.Fore.RED+"\nNo hay datos registrados.\n")
    elif Opcion == "5":
        ruta = get_ruta()
        usuariosContrasenias = load_players(ruta, usuariosContrasenias)
    elif Opcion == "0":
        print("")
    else:
        print(cl.Fore.RED+"\nvalor no valido\n")