class Ruta:
    def __init__(self, grado, energia, tecnica, fuerza):
        self.grado = grado
        self.energia = energia
        self.tecnica = tecnica
        self.fuerza = fuerza
        
    def __str__(self):
        return f"{self.grado}_{self.energia}"
    
    def __repr__(self):
        return self.__str__()