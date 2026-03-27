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
    c.crear_carta(personaje['nombre'], randint(0,5), randint(0,3), "")

    cartas.append(c)
    personajes.remove(personaje)

for c in cartas:
    print(c)


