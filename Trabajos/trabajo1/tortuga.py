from random import choice

class Tortuga:
    def __init__(self):
        self.nombre = ""
        self.velocidad = 0
        self.posicion_carrera = 0
        self.distancia_recorrida = 0
        self.frase_ganador = ""
        self.frase_top3 = ""
        self.frase_perdedor = ""
        self.avanza= True
        self.si_no_abanza= 0

    def crear_tortuga(self, nombre, frase1, frase2, frase3):
        self.nombre = nombre
        self.frase_ganador = frase1
        self.frase_top3 = frase2
        self.frase_perdedor = frase3

