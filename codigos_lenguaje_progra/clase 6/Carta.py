from random import choice

class Carta:
    def __init__(self):
        self.nombre = ""
        self.fuerza = 0
        self.coste = 0
        self.habilidad = ""
    

    def crear_carta(self, nombre, fuerza, coste, habilidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.coste = coste
        self.habilidad = habilidad
    
    def asignar_abilidad(self):
        habilidades = [
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

        habilidad = choice(habilidades)

        self.habilidad = list(habilidad.keys())[0]


    
