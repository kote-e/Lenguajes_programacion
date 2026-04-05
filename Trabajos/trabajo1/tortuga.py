from random import choice

class Tortuga:
    def __init__(self):
        self.nombre = ""
        self.velocidad = 0
        self.posicion_carrera = 0
        self.distancia_recorrida = 0
        self.frase = ""
        self.avanza= True
        self.si_no_abanza= 0

    def crear_tortuga(self, nombre, frase):
        self.nombre = nombre
        self.frase = frase

