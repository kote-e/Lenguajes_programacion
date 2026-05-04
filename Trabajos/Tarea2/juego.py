# importar las clases necesarias para el juego
from Tablero import Tablero
from Peon import Peon
from Torre import Torre
from Alfil import Alfil
from Caballo import Caballo
from Reina import Reina
from Rey import Rey


#comprueba si la pieza seleccionada es válida para mover, que exista, que sea del color correcto y que tenga movimientos posibles.
def comprobar_siesmovible(pieza, color):
    if pieza is None:
        print("¡No hay ninguna pieza en esa posición! Intenta de nuevo.")
        return False
    elif pieza.color != color:
        print(f"¡Esa no es una pieza {color}! Intenta de nuevo.")
        return False
    elif not pieza.movimientos_posibles(tablero):
        print("¡Esa pieza no tiene movimientos posibles! Intenta de nuevo.")
        return False
    else:
        return True

def comprobar_movimiento_valido(pieza, fila_destino, col_destino):
    if (fila_destino, col_destino) in pieza.movimientos_posibles(tablero):
        return True
    else:
        print("¡Movimiento no válido para esa pieza! Intenta de nuevo.")
        return False
    
def turnos(color):
   comprovar=True
   while comprovar:
        mover = input("Ingrese la pieza que quiere mover ejemplo (a6): ")
        mover = mover.strip()
        columna = ord(mover[0].lower()) - ord('a')
        fila = tablero._fila - int(mover[1:])
        #print(f"Columna: {columna}, Fila: {fila}")
        if columna < 0 or columna >= tablero._columna or fila < 0 or fila >= tablero._fila:
            print("¡Posición fuera de los límites del tablero! Intenta de nuevo.")
            continue

        pieza = tablero.obtener_pieza(fila, columna)
        if comprobar_siesmovible(pieza, color):
            comprovar=False
        else:
            print("Intenta de nuevo.")
    
        tablero.mostrar_movimientos(pieza)
        destino = input("Ingrese la posición de destino: ")
        col_destino = ord(destino[0].lower()) - ord('a')
        fila_destino = int(destino[1])

        tablero.mover_pieza(pieza, fila_destino, col_destino)
        tablero.imprimir()
   
def colocar_piesas_iniciales(tablero):
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


print("\033[1;3;35m ¡¡Inicio del juego!!  \033[0m")

tablero= Tablero(8, 8)
colocar_piesas_iniciales(tablero)
tablero.imprimir()

turno_actual= 0
jugar= True
while jugar:
    if turno_actual % 2 == 0:
        print("\033[1;3;35m Turno de las piezas blancas!!  \033[0m")
        turnos("blanco")
        
    else:
        print("\033[1;3;35m Turno de las piezas negras!!  \033[0m")
        turnos("negro")

    turno_actual += 1