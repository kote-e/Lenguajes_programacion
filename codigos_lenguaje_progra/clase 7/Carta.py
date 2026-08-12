from random import choice

class Carta:
    def __init__(self):
        self.nombre = ""
        self.fuerza = 0
        self.coste = 0
        self.habilidad = ""
    
        self.habilidades = [
            {
                "super sayayin": 2
            },
            {
                "roba alma": -2
            },
            {
                "quemadura": True
            },
            {
                "nada": 0
            }
        ]
    
    def __str__(self):
        return self.nombre

    def crear_carta(self, nombre, fuerza, coste, habilidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.coste = coste
        self.habilidad = habilidad
    
    def asignar_abilidad(self):
        habilidad = choice(self.habilidades)

        self.habilidad = list(habilidad.keys())[0]

    def sayayin(self):
        self.fuerza += 2

    def roba_alma(self, carta):
        carta.fuerza -= 2



    
