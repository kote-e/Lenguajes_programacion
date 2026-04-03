from random import choice

class Tortuga:
    def __init__(self):
        self.nombre = ""
        self.velocidad = 0
        self.posicion_carrera = 0
        self.distancia_recorrida = 0
        self.frase = ""

    def crear_tortuga(self, nombre, velocidad, frase):
        self.nombre = nombre
        self.velocidad = velocidad
        self.frase = frase
