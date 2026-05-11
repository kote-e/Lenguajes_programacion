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
   


# Implementar la lógica para verificar si el rey de un color está en jaque
def Jaque(tablero, color, rey):
    reydir= rey.obtener_rey()

    for i in range(tablero._fila):
        for j in range(tablero._columna):
            piezas= tablero.obtener_pieza(i, j)
            if piezas.color != color:
               comprovar= tablero.mostrar_movimientos(piezas)
               if reydir in comprovar:
                   print(f"¡El rey {color} está en jaque!")
                   return True
            else:
                continue
    return False
    

  

print("\033[1;3;35m ¡¡Inicio del juego!!  \033[0m")

tablero= Tablero(8, 8)
#piezas blancas
peon_blanco1 = Peon("blanco")
peon_blanco2 = Peon("blanco")
peon_blanco3 = Peon("blanco")
peon_blanco4 = Peon("blanco")
peon_blanco5 = Peon("blanco")
peon_blanco6 = Peon("blanco")
peon_blanco7 = Peon("blanco")
peon_blanco8 = Peon("blanco")
torre_blanco1 = Torre("blanco")
torre_blanco2 = Torre("blanco")
alfil_blanco1 = Alfil("blanco")
alfil_blanco2 = Alfil("blanco")
caballo_blanco1 = Caballo("blanco")
caballo_blanco2 = Caballo("blanco")
reina_blanca1 = Reina("blanco")
rey_blanco1 = Rey("blanco")
peones_blancos= [peon_blanco1, peon_blanco2, peon_blanco3, peon_blanco4, peon_blanco5, peon_blanco6, peon_blanco7, peon_blanco8]

#piezas negras
peon_negro1 = Peon("negro")
peon_negro2 = Peon ("negro")
peon_negro3 = Peon ("negro")
peon_negro4 = Peon ("negro")
peon_negro5 = Peon ("negro")
peon_negro6 = Peon ("negro")
peon_negro7 = Peon ("negro")
peon_negro8 = Peon ("negro")
torre_negro1 = Torre("negro")
torre_negro2 = Torre("negro")
alfil_negro1 = Alfil("negro")
alfil_negro2 = Alfil("negro")
caballo_negro1 = Caballo("negro")
caballo_negro2 = Caballo("negro")
reina_negra1 = Reina("negro")
rey_negro1 = Rey("negro")
peones_negros= [peon_negro1, peon_negro2, peon_negro3, peon_negro4, peon_negro5, peon_negro6, peon_negro7, peon_negro8]
#colocar piezas blancas
for i in range (len(peones_blancos)):
    tablero.colocar_pieza(peones_blancos[i], fila=6, col=i)
tablero.colocar_pieza(torre_blanco1, fila=7, col=0)
tablero.colocar_pieza(torre_blanco2, fila=7, col=7)
tablero.colocar_pieza(alfil_blanco1, fila=7, col=2)
tablero.colocar_pieza(alfil_blanco2, fila=7, col=5)
tablero.colocar_pieza(caballo_blanco1, fila=7, col=1)
tablero.colocar_pieza(caballo_blanco2, fila=7, col=6)
tablero.colocar_pieza(reina_blanca1, fila=7, col=3)
tablero.colocar_pieza(rey_blanco1, fila=7, col=4)
    
#colocar piezas negras
for i in range (len(peones_negros)):
    tablero.colocar_pieza(peones_negros[i], fila=1, col=i)
tablero.colocar_pieza(torre_negro1, fila=0, col=0)
tablero.colocar_pieza(torre_negro2, fila=0, col=7)
tablero.colocar_pieza(alfil_negro1, fila=0, col=2)
tablero.colocar_pieza(alfil_negro2, fila=0, col=5)
tablero.colocar_pieza(caballo_negro1, fila=0, col=1)
tablero.colocar_pieza(caballo_negro2, fila=0, col=6)
tablero.colocar_pieza(reina_negra1, fila=0, col=3)
tablero.colocar_pieza(rey_negro1, fila=0, col=4)

tablero.imprimir()

turno_actual= 0
jugar= True
while jugar:
    if turno_actual % 2 == 0:
        print("\033[1;3;97m Turno de las piezas blancas!!  \033[0m")
        
        hay_jaque= Jaque(tablero, "blanco", rey_blanco1)# comprobar si el rey blanco está en jaque
        turnos("blanco")

        
    else:
        print("\033[1;3;90m Turno de las piezas negras!!  \033[0m")
        hay_jaque= Jaque(tablero, "negro", rey_negro1) # comprobar si el rey negro está en jaque
        turnos("negro")
        

    turno_actual += 1