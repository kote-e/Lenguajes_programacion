class Reina:
    def __init__(self, color):
        self._fila = None
        self._col = None
        self.color = color
    
    def __str__(self):
        return "♕" if self.color == "blanco" else "♛"
    
    def movimientos_posibles(self, tablero):
        """Retorna lista de (fila, col) a los que puede moverse."""
        movimientos=[]
        f, c  = self._fila, self._col

        # Movimientos verticales y horizontales (como torre)
        if 0 <= f < tablero._fila:
            # Hacia abajo
            for i in range(f+1, tablero._fila):
                if tablero.celda_libre(i, c):
                    movimientos.append((i, c))
                elif tablero.hay_enemigo(i, c, self.color):
                    movimientos.append((i, c))
                    break
                else:
                    break
            # Hacia arriba
            for i in range(f-1, -1, -1):
                if tablero.celda_libre(i, c):
                    movimientos.append((i, c))
                elif tablero.hay_enemigo(i, c, self.color):
                    movimientos.append((i, c))
                    break
                else:
                    break
        # Movimientos horizontales
        if 0 <= c < tablero._columna:
            # Hacia la derecha
            for j in range(c+1, tablero._columna):
                if tablero.celda_libre(f, j):
                    movimientos.append((f, j))
                elif tablero.hay_enemigo(f, j, self.color):
                    movimientos.append((f, j))
                    break
                else:
                    break
            # Hacia la izquierda
            for j in range(c-1, -1, -1):
                if tablero.celda_libre(f, j):
                    movimientos.append((f, j))
                elif tablero.hay_enemigo(f, j, self.color):
                    movimientos.append((f, j))
                    break
                else:
                    break
        # Movimientos diagonales (como alfil)
        for diagonal in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            df, dc = diagonal[0], diagonal[1]
            for i in range(1, max(tablero._fila, tablero._columna)):
                nf, nc = f + df * i, c + dc * i
                if 0 <= nf < tablero._fila and 0 <= nc < tablero._columna:
                    if tablero.celda_libre(nf, nc):
                        movimientos.append((nf, nc))
                    elif tablero.hay_enemigo(nf, nc, self.color):
                        movimientos.append((nf, nc))
                        break
                    else:
                        break
                else:
                    break
            
        return movimientos