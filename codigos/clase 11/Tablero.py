class Tablero:
    _BLANCA = "\033[47m"   # fondo blanco
    _NEGRA  = "\033[100m"  # fondo gris oscuro
    _VERDE  = "\033[42m"   # fondo verde (movimiento posible)
    _RESET  = "\033[0m"

    def __init__(self):
        self._grid = [[None] * 8 for i in range(8)]
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

    def imprimir(self):
        print("\n    a   b   c   d   e   f   g   h")
        print("  +" + "---+" * 8)
        for fila in range(8):
            print(f"{8 - fila} |", end="")
            for col in range(8):
                pieza   = self._grid[fila][col]
                simbolo = str(pieza) if pieza else " "
                fondo   = self._VERDE if (fila, col) in self._marcadas else self._color_casilla(fila, col)
                print(f"{fondo} {simbolo} {self._RESET}|", end="")
            print(f" {8 - fila}")
        print("  +" + "---+" * 8)
        print("    a   b   c   d   e   f   g   h\n")
