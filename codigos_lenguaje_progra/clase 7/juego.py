import json
from random import choice, randint
from Carta import Carta

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

# for c in cartas:
#     print(c.fuerza, c.habilidad)

carta1 = choice(cartas)
cartas.remove(carta1)
carta2 = choice(cartas)
cartas.remove(carta2)

duelo = [carta1, carta2]

for d in duelo:
    indice = duelo.index(d)

    if d.habilidad == "super sayayin":
        d.sayayin()

    if d.habilidad == "roba alma":
        d.roba_alma(duelo[indice - 1])

print(f"Se van a enfrentar {carta1} vs {carta2}")
if carta1.fuerza > carta2.fuerza:
    print(f"Gano {carta1}")
elif carta2.fuerza > carta1.fuerza:
    print(f"Gano {carta2}")
else:
    if carta1.habilidad == "quemadura" and carta2.habilidad == "quemadura":
        print("Empataron")
    elif carta1.habilidad == "quemadura":
        print(f"Gano {carta1}")
    elif carta2.habilidad == "quemadura":
        print(f"Gano {carta2}")
    else:
        print("Empataron")





