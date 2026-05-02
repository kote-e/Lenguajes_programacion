class Rey:
    def __init__(self, color):
        self._fila = None
        self._col = None
        self.color = color
    
    def __str__(self):
        return "♔" if self.color == "blanco" else "♚" 
    
    def movimientos_posibles(self, tablero):
        """Retorna lista de (fila, col) a los que puede moverse."""
        movs      = []
        f, c      = self._fila, self._col
        # Movimientos en las 8 direcciones
        for df in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if df == 0 and dc == 0:
                    continue
                nf, nc = f + df, c + dc
                if 0 <= nf < tablero._fila and 0 <= nc < tablero._columna:
                    if tablero.celda_libre(nf, nc) or tablero.hay_enemigo(nf, nc, self.color):
                        movs.append((nf, nc))
        return movs