class Peon:
    def __init__(self, color):
        self._fila = None
        self._col = None
        self.color = color
        self._movido = False
        self.estado = "activo"
        # self.id = id


    def __str__(self):
        return "♙" if self.color == "blanco" else "♟"
    
    # def __repr__(self):
    #     return f"Peon {self.color}"
    
    def movimientos_posibles(self, tablero):
        """Retorna lista de (fila, col) a los que puede moverse."""
        movs      = []
        direccion = -1 if self.color == "blanco" else 1   # blanco sube, negro baja
        f, c      = self._fila, self._col
        sig_fila  = f + direccion

        # avance simple
        if 0 <= sig_fila < tablero._fila and tablero.celda_libre(sig_fila, c):
            movs.append((sig_fila, c))

            # avance doble desde posición inicial
            if not self._movido:
                doble = f + 2 * direccion
                if 0 <= doble < tablero._fila and tablero.celda_libre(doble, c):
                    movs.append((doble, c))

        # capturas en diagonal
        for dc in [-1, 1]:
            nc = c + dc
            if 0 <= sig_fila < tablero._fila and 0 <= nc < tablero._columna:
                if tablero.hay_enemigo(sig_fila, nc, self.color):
                    movs.append((sig_fila, nc))

        return movs
    
