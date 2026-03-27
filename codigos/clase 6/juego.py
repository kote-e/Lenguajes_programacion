import json
from random import choice, randint
from Carta import Carta

from colorama import Fore, Style, init
init()

# c = Carta()
# print(c.nombre, c.fuerza)

with open("personajes.json", "r") as f:
    personajes = json.load(f)

cartas = []

for i in range(10):
    personaje = choice(personajes)
    c = Carta()
    c.crear_carta(personaje["nombre"], randint(0,5), randint(0,3), "")
    c.asignar_abilidad()
    cartas.append(c)
    personajes.remove(personaje)


ganadores = []
for i in range(len(cartas)//2): # se repite la mitad de las cartas para que haya 2 personajes iguales
    personajes=[choice(cartas)] # se elige un personaje al azar de la lista de cartas para el combate
    cartas.remove(personajes[0])# se elimina el personaje elegido de la lista de cartas para que no se repita en el siguiente combate
    personajes.append(choice(cartas)) # se elige otro personaje al azar de la lista de cartas para el combate
    cartas.remove(personajes[1]) # se elimina el personaje elegido de la lista de cartas para que no se repita en el siguiente combate

    #iniciar combate
    print(Style.BRIGHT + Fore.YELLOW + "⚔️  Se ha iniciado un combate ⚔️".center(50) + Style.RESET_ALL)
    print(Fore.YELLOW +  f"{personajes[0].nombre} con fuerza {personajes[0].fuerza} y habilidad {personajes[0].habilidad}"+ Style.RESET_ALL + Fore.RED + " vs" + Style.RESET_ALL + Fore.YELLOW + f" {personajes[1].nombre} con fuerza {personajes[1].fuerza} y habilidad {personajes[1].habilidad}" + Style.RESET_ALL)
   

    #comparar habilidades
    for i in range(len(personajes)):
        if personajes[i].habilidad == "super sayayin":
            personajes[i].fuerza += 2
        elif personajes[i].habilidad == "roba alma":
            personajes[i-1].fuerza -= 2
        else:
            continue
    
    #comparar fuerzas
    if personajes[0].fuerza > personajes[1].fuerza:
        print(f"{personajes[0].nombre} ha ganado el combate")
        ganadores.append(personajes[0])
    elif personajes[0].fuerza < personajes[1].fuerza:
        print(f"{personajes[1].nombre} ha ganado el combate")
        ganadores.append(personajes[1])
    else:
        if personajes[0].habilidad == "quemadura" and personajes[1].habilidad != "quemadura":
            print(f"{personajes[0].nombre} ha ganado el combate por quemadura")
            ganadores.append(personajes[0])
        elif personajes[1].habilidad == "quemadura" and personajes[0].habilidad != "quemadura":
            print(f"{personajes[1].nombre} ha ganado el combate por quemadura")
            ganadores.append(personajes[1])
        else:
            print("El combate ha terminado en empate")
            ganadores.append(personajes[0])
            ganadores.append(personajes[1])
    print("="*50)
    print("="*50) # separador entre combates

print(Style.BRIGHT + Fore.CYAN + "\n🏆 GANADORES 🏆".center(50) + Style.RESET_ALL)
for ganador in ganadores:
    print(Fore.RED + f"-" + Style.RESET_ALL + f" {ganador.nombre}")






