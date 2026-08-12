class Caballo:
    def __init__(self, color):
        self.color = color
        self._movido = False
        self.estado = "activo"

    def __str__(self):
        return "♘" if self.color == "blanco" else "♞"

    def movimientos_posibles(self, tablero,):
        """Retorna lista de (fila, col) a los que puede moverse."""
        movimientos = []
        fila, col = self._fila, self._col
        # Movimientos en "L"
        for direction in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
            nf, nc = fila + direction[0], col + direction[1]
            if 0 <= nf < tablero._fila and 0 <= nc < tablero._columna:
                if tablero.celda_libre(nf, nc) or tablero.hay_enemigo(nf, nc, self.color):
                    movimientos.append((nf, nc))
        return movimientos
    