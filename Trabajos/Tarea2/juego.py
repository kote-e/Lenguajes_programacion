from Tablero import Tablero
from Peon import Peon
from Torre import Torre
from Alfil import Alfil
from Caballo import Caballo
from Reina import Reina
from Rey import Rey

''' Pruebas de cada pieza y del tablero. '''
# tablero= Tablero(8, 8)
# tablero.imprimir()

# Crear peones blancos
# peon_blanco1 = Peon("blanco")
# peon_negro1 = Peon("negro")

# torre_blanca1= Torre("blanco")
# torre_negra1= Torre("negro")

# alfil_blanco1 = Alfil("blanco")
# alfil_negro1 = Alfil("negro")

# Caballo_blanco1 = Caballo("blanco")
# Caballo_negro1 = Caballo("negro")

# reina_blanca1 = Reina("blanco")
# reina_negra1 = Reina("negro")

# tablero.colorcar_pieza(peon_blanco1, fila=6, col=3)
# tablero.colorcar_pieza(peon_negro1, fila=1, col=3)
# tablero.colorcar_pieza(torre_blanca1, fila=7, col=0)
# tablero.colorcar_pieza(torre_negra1, fila=0, col=0)
# tablero.colorcar_pieza(alfil_blanco1, fila=7, col=2)
# tablero.colorcar_pieza(alfil_negro1, fila=0, col=2)
# tablero.colorcar_pieza(Caballo_blanco1, fila=7, col=1)
# tablero.colorcar_pieza(Caballo_negro1, fila=0, col=1)
# tablero.colorcar_pieza(reina_blanca1, fila=7, col=3)
# tablero.colorcar_pieza(reina_negra1, fila=0, col=3)
# tablero.imprimir()



# print("Movimientos posibles:")

# tablero.mostrar_movimientos(peon_blanco1)
# tablero.mostrar_movimientos(torre_blanca1)
# tablero.mostrar_movimientos(torre_negra1)
# tablero.mostrar_movimientos(peon_negro1)
# tablero.mostrar_movimientos(alfil_blanco1)
# tablero.mostrar_movimientos(alfil_negro1)   
# tablero.mostrar_movimientos(Caballo_blanco1)
# tablero.mostrar_movimientos(Caballo_negro1)
# tablero.mostrar_movimientos(reina_blanca1)
# tablero.mostrar_movimientos(reina_negra1)
#tablero.imprimir()

print("\033[1;3;35m ¡¡Inicio del juego!!  \033[0m")

tablero= Tablero(8, 8)
# Crear peones blancos
for i in range (8):
    tablero.colorcar_pieza(Peon("blanco"), fila=6, col=i)

    tablero.colorcar_pieza(Peon("negro"), fila=1, col=i)

for i in range(8):
    if i == 0 or i == 7:
        tablero.colorcar_pieza(Torre("blanco"), fila=7, col=i)

        tablero.colorcar_pieza(Torre("negro"), fila=0, col=i)
    elif i == 1 or i == 6:
        tablero.colorcar_pieza(Caballo("blanco"), fila=7, col=i)

        tablero.colorcar_pieza(Caballo("negro"), fila=0, col=i)
    elif i == 2 or i == 5:
        tablero.colorcar_pieza(Alfil("blanco"), fila=7, col=i)

        tablero.colorcar_pieza(Alfil("negro"), fila=0, col=i)
    elif i == 3:
        tablero.colorcar_pieza(Reina("blanco"), fila=7, col=i)

        tablero.colorcar_pieza(Reina("negro"), fila=0, col=i)
    elif i == 4:
        tablero.colorcar_pieza(Rey("blanco"), fila=7, col=i)

        tablero.colorcar_pieza(Rey("negro"), fila=0, col=i)
tablero.imprimir()
turnos= ["blanco", "negro"]
turno_actual= 0
jugar= True
while jugar:
    if turno_actual % 2 == 0:
        print("\033[1;3;35m Turno de las piezas blancas!!  \033[0m")
        mover = input("Ingrese la pieza: ") 
        columna = ord(mover[0].lower()) - ord('a')
        fila =  int(mover[1])
        pieza = tablero.obtener_pieza(fila, columna)
        tablero.mostrar_movimientos(pieza)


        destino = input("Ingrese la posición de destino: ")
        col_destino = ord(destino[0].lower()) - ord('a')
        fila_destino = int(destino[1])
        tablero.mover_pieza(pieza, fila_destino, col_destino)
        tablero.imprimir()

    else:
        print("\033[1;3;35m Turno de las piezas negras!!  \033[0m")

    turno_actual += 1