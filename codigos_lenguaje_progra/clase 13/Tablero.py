class Tablero:
    _OCULTA      = "\033[100m"  # gris oscuro
    _SELECCIONADA = "\033[43m"  # amarillo
    _ENCONTRADA  = "\033[42m"   # verde
    _RESET       = "\033[0m"

    def __init__(self, filas, cols):
        self.filas = filas
        self.cols = cols
        self._grid = [[None] * cols for i in range(filas)]

    def _color(self, ficha, pos, seleccionadas):
        """Decide qué color de fondo usar para una ficha."""
        if pos in seleccionadas:
            return self._SELECCIONADA
        if ficha.encontrada:
            return self._ENCONTRADA
        return self._OCULTA
    
    def colocar(self, ficha, fila, col):
        self._grid[fila][col] = ficha

    def ficha_en(self, fila, col):
        return self._grid[fila][col]

    def imprimir(self, seleccionadas=None):
        seleccionadas = seleccionadas or []

        # encabezado de columnas: 1, 2, 3...
        print("\n    ", end="")
        for c in range(self.cols):
            print(f"  {c + 1} ", end="")
        print()

        # filas: A, B, C...
        for f in range(self.filas):
            print(f"  {chr(65 + f)} ", end="")
            for c in range(self.cols):
                ficha = self._grid[f][c]
                fondo = self._color(ficha, (f, c), seleccionadas)
                print(f"{fondo} {ficha} {self._RESET}", end=" ")
            print()
        print()