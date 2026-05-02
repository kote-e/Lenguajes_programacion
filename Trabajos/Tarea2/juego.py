from Tablero import Tablero
from Peon import Peon
from Torre import Torre
from Alfil import Alfil
from Caballo import Caballo
from Reina import Reina

tablero= Tablero(8, 8)
tablero.imprimir()

# Crear peones blancos
peon_blanco1 = Peon("blanco")
peon_negro1 = Peon("negro")

torre_blanca1= Torre("blanco")
torre_negra1= Torre("negro")

alfil_blanco1 = Alfil("blanco")
alfil_negro1 = Alfil("negro")

Caballo_blanco1 = Caballo("blanco")
Caballo_negro1 = Caballo("negro")

reina_blanca1 = Reina("blanco")
reina_negra1 = Reina("negro")

tablero.colorcar_pieza(peon_blanco1, fila=6, col=3)
tablero.colorcar_pieza(peon_negro1, fila=1, col=3)
tablero.colorcar_pieza(torre_blanca1, fila=7, col=0)
tablero.colorcar_pieza(torre_negra1, fila=0, col=0)
tablero.colorcar_pieza(alfil_blanco1, fila=7, col=2)
tablero.colorcar_pieza(alfil_negro1, fila=0, col=2)
tablero.colorcar_pieza(Caballo_blanco1, fila=7, col=1)
tablero.colorcar_pieza(Caballo_negro1, fila=0, col=1)
tablero.colorcar_pieza(reina_blanca1, fila=7, col=3)
tablero.colorcar_pieza(reina_negra1, fila=0, col=3)
tablero.imprimir()



print("Movimientos posibles:")

tablero.mostrar_movimientos(peon_blanco1)
tablero.mostrar_movimientos(torre_blanca1)
tablero.mostrar_movimientos(torre_negra1)
tablero.mostrar_movimientos(peon_negro1)
tablero.mostrar_movimientos(alfil_blanco1)
tablero.mostrar_movimientos(alfil_negro1)   
tablero.mostrar_movimientos(Caballo_blanco1)
tablero.mostrar_movimientos(Caballo_negro1)
tablero.mostrar_movimientos(reina_blanca1)
tablero.mostrar_movimientos(reina_negra1)
#tablero.imprimir()