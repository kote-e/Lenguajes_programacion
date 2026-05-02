class Tablero:
    _BLANCA = "\033[47m"   # fondo blanco
    _NEGRA  = "\033[100m"  # fondo gris oscuro
    _VERDE  = "\033[42m"   # fondo verde (movimiento posible)
    _RESET  = "\033[0m"

    def __init__(self, fila, columna):
        self._fila = fila
        self._columna = columna
        self._grid = [[None] * columna for i in range(fila)] 
        self._marcadas = set()
        
    def _color_casilla(self, fila, columna):
        if (fila + columna) % 2 == 0:
            return self._BLANCA
        return self._NEGRA
    

    def hay_enemigo(self, fila, col, color_amigo):
        """Retorna True si la celda tiene una pieza de color distinto."""
        pieza = self._grid[fila][col]
        return pieza is not None and pieza.color != color_amigo

    def mostrar_movimientos(self, pieza):
        """Pide a la pieza sus movimientos, los marca y muestra el tablero."""
        self._marcadas = set(pieza.movimientos_posibles(self))
        self.imprimir()
        self._marcadas = set()

    def celda_libre(self, fila, col):
        return self._grid[fila][col] is None
    
    def colorcar_pieza(self, pieza, fila, col):
        self._grid[fila][col] = pieza
        pieza._fila = fila
        pieza._col  = col
    
    def mover_pieza(self, pieza, fila_destino, col_destino):
        if (fila_destino, col_destino) in pieza.movimientos_posibles(self):
            self._grid[pieza._fila][pieza._col] = None  # quitar de la posición actual
            self.colorcar_pieza(pieza, fila_destino, col_destino)
        else:
            print("Movimiento no válido para esa pieza.")
    
    def obtener_pieza(self, fila, col):
        return self._grid[fila][col]

    def imprimir(self):
        letras = "abcdefghijklmnopqrstuvwxyz"
        print("\n    " + "   ".join(letras[:self._columna]))
        print("   +" + "---+" * self._columna)
        for fila in range(self._fila):
            if self._fila - fila < 10:
                print(f" {self._fila - fila} |", end="")
            else:
                print(f" {self._fila - fila}|", end="")
            for col in range(self._columna):
                pieza   = self._grid[fila][col]
                simbolo = str(pieza) if pieza else " "
                fondo   = self._VERDE if (fila, col) in self._marcadas else self._color_casilla(fila, col)
                fondo = fondo.replace("m", ";97m") if pieza and pieza.color == "blanco" else fondo.replace("m", ";90m")
                print(f"{fondo} {simbolo} {self._RESET}|", end="")
            print(f" {self._fila - fila}")
        print("   +" + "---+" * self._columna)
        print("    " + "   ".join(letras[:self._columna]) + "\n")
