class Escalador:
    def __init__(self, nombre, energia, tecnica, fuerza):
        self.nombre = nombre
        self.energia = energia
        self.tecnica = tecnica
        self.fuerza = fuerza

        self.grado_mas_dificil = None
        self.contador_rutas = 0
        
    def __str__(self):
        return self.nombre
    
    def __repr__(self):
        return self.__str__()