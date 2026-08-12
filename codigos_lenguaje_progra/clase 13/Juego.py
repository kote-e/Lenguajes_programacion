import random
import time
from Tablero import Tablero
from Ficha import Ficha

class Juego:
    def __init__(self, filas, cols):
        self._tablero = Tablero(filas, cols)
        self._turnos        = 0
        self._parejas       = 0
        self._total_parejas = (filas * cols) // 2
        self._preparar()

    def _preparar(self):
        """Crea los pares de fichas, los mezcla y los coloca en el tablero."""
        letras  = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        valores = letras[:self._total_parejas] * 2
        random.shuffle(valores)

        for f in range(self._tablero.filas):
            for c in range(self._tablero.cols):
                foo = Ficha(valores.pop())
                foo.voltear()
                self._tablero.colocar(foo, f, c)

    def _pedir_posicion(self, numero):
        """Pide y valida una posición al jugador. Retorna (fila, col)."""
        while True:
            entrada = input(f"  Ficha {numero} (ej. A3): ").strip().upper()

            if len(entrada) < 2:
                print("  Entrada inválida.")
                continue

            fila = ord(entrada[0]) - 65
            try:
                col = int(entrada[1:]) - 1
            except ValueError:
                print("  Entrada inválida.")
                continue

            if not (0 <= fila < self._tablero.filas and 0 <= col < self._tablero.cols):
                print("  Posición fuera del tablero.")
                continue

            ficha = self._tablero.ficha_en(fila, col)

            if ficha.encontrada:
                print("  Esa pareja ya fue encontrada.")
                continue

            if ficha.visible:
                print("  Esa ficha ya está seleccionada.")
                continue

            return fila, col
        
    def _turno(self):
        """Ejecuta un turno completo: dos selecciones y evaluación."""
        # primera ficha
        f1, c1 = self._pedir_posicion(1)
        ficha1  = self._tablero.ficha_en(f1, c1)
        ficha1.voltear()
        self._tablero.imprimir(seleccionadas=[(f1, c1)])

        # segunda ficha
        f2, c2 = self._pedir_posicion(2)
        ficha2  = self._tablero.ficha_en(f2, c2)
        ficha2.voltear()
        self._tablero.imprimir(seleccionadas=[(f1, c1), (f2, c2)])

        self._turnos += 1

        if ficha1.valor == ficha2.valor:
            print("  ¡Pareja encontrada!\n")
            ficha1.marcar_pareja()
            ficha2.marcar_pareja()
            self._parejas += 1
        else:
            print("  No es pareja. Memorízalas...\n")
            time.sleep(2)
            ficha1.voltear()
            ficha2.voltear()

    def jugar(self):
        print("\r\n=== MEMORICE ===", end="")
        print(f"\rTablero {self._tablero.filas}x{self._tablero.cols} — {self._total_parejas} parejas\n", end="")

        while self._parejas < self._total_parejas:
            self._tablero.imprimir()
            print(f"\r  Turno {self._turnos + 1}  |  Parejas: {self._parejas}/{self._total_parejas}\n", end="")
            # self._turno()
            break

        self._tablero.imprimir()
        print(f"\r  ¡Ganaste en {self._turnos} turnos!", end="")