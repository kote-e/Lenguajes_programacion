from Juego import Juego
from Tablero import Tablero
from Ficha import Ficha

# # Prueba rápida
f = Ficha("A")
print(f._encontrada)
# # print(f.encontrada)
# # print(f"Recién creada:   {f}")       # ?
# f.voltear()
# # print(f"Volteada:        {f}")       # A
# # f.voltear()
# # print(f"Vuelta abajo:    {f}")       # ?
# # f.marcar_pareja()
# # print(f"Encontrada:      {f}")       # A

t = Tablero(1,1)
print(t._grid)
# t.colocar(f, 0, 0)
# t.imprimir([(0,0)])

j = Juego(2,5)
j.jugar()