class Carta:
    def __init__(self):
        self.nombre = ""
        self.fuerza = 0
        self.coste = 0
        self.habilidad = ""
    
    def __str__(self): 
        return f"{self.nombre} {self.fuerza}"

    def crear_carta(self, nombre, fuerza, coste, habilidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.coste = coste
        self.habilidad = habilidad
    
    def print_carta(self):
        print(self.nombre, self.fuerza, self.coste, self.habilidad)


