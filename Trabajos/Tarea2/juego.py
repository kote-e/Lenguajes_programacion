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

def comprobar_peon(tablero, pieza):
        if "Peon" in str(type(pieza)):
            print(pieza._movido)
            if pieza._movido == False:
                pieza._movido= True
            if pieza.color== "blanco":
                final= 0
            else:
                final= tablero._fila
            if pieza._fila== final: 
                pieza.estado= "desactivo"
            print(pieza.estado, pieza._movido)
    
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
    fila_destino = tablero._fila - int(destino[1])

    tablero.mover_pieza(pieza, fila_destino, col_destino)
    comprobar_peon(tablero, pieza)
    tablero.imprimir()
   


# Implementar la lógica para verificar si el rey de un color está en jaque
def Jaque(tablero, color, rey):
    reydir= rey.obtener_rey()

    for i in range(tablero._fila):
        for j in range(tablero._columna):
            piezas= tablero.obtener_pieza(i, j)
            if piezas is not None and piezas.estado == "activo":
                if piezas.color != color:
                    comprobar= tablero.mostrar_movimientos(piezas)
                    if comprobar is not None:
                        if reydir in comprobar:
                            print(f"¡El rey {color} está en jaque!")
                            return True
                        else:
                            continue
    return False
    
def colocar_piesas_iniciales(tablero):
    for i in range (8):
        tablero.colocar_pieza(Peon("blanco"), fila=6, col=i)
        tablero.colocar_pieza(Peon("negro"), fila=1, col=i)
    for i in range(8):
        if i == 0 or i == 7:
            tablero.colocar_pieza(Torre("blanco"), fila=7, col=i)
            tablero.colocar_pieza(Torre("negro"), fila=0, col=i)
        elif i == 1 or i == 6:
            tablero.colocar_pieza(Caballo("blanco"), fila=7, col=i)
            tablero.colocar_pieza(Caballo("negro"), fila=0, col=i)
        elif i == 2 or i == 5:
            tablero.colocar_pieza(Alfil("blanco"), fila=7, col=i)
            tablero.colocar_pieza(Alfil("negro"), fila=0, col=i)
        elif i == 3:
            tablero.colocar_pieza(Reina("blanco"), fila=7, col=i)
            tablero.colocar_pieza(Reina("negro"), fila=0, col=i)

  

print("\033[1;3;35m ¡¡Inicio del juego!!  \033[0m")

tablero= Tablero(8, 8)
colocar_piesas_iniciales(tablero)

#colocar los reyes después de colocar las demás piezas para evitar que se marquen como en jaque al inicio del juego
rey_blanco1 = Rey("blanco")
rey_negro1 = Rey("negro")
tablero.colocar_pieza(rey_blanco1, fila=7, col=4)
tablero.colocar_pieza(rey_negro1, fila=0, col=4)
tablero.imprimir()

turno_actual= 0
jugar= True
while jugar:
    if turno_actual % 2 == 0:
        print("\033[1;3;97m Turno de las piezas blancas!!  \033[0m")
        hay_jaque= Jaque(tablero, "blanco", rey_blanco1) # comprobar si el rey blanco está en jaque
        turnos("blanco")
  
    else:
        print("\033[1;3;90m Turno de las piezas negras!!  \033[0m")
        hay_jaque= Jaque(tablero, "negro", rey_negro1) # comprobar si el rey negro está en jaque
        turnos("negro")
        
    turno_actual += 1