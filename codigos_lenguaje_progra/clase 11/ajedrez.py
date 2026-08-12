from Tablero import Tablero
from Peon import Peon
from random import randint

tablero = Tablero()
tablero.imprimir()

peones = []

for i in range(10):
    rand = randint(1, 100)
    peon = Peon("blanco")
    peones.append(peon)

print(peones)

set_peones = set(peones)

print(set_peones)


# peon._movido = True
# tablero.colorcar_pieza(peon, 4, 4)

# tablero.imprimir()
# print("Movimientos posibles del peón:")
# tablero.mostrar_movimientos(peon)