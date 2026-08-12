class Ruta:
    def __init__(self, grado, tecnica, fuerza, energia):
        self.grado = grado
        self.tecnica = tecnica
        self.fuerza = fuerza
        self._energia = energia
        
        self._intentos = 0
    
    @property
    def energia(self):
        return self._energia
    
    #se ignora el valor ingresado y se mantiene el valor actual de energia
    @energia.setter
    def energia(self, valor):
        if valor >  0:
            self._energia = valor
        else:
            self._energia = self._energia           
    
    #intentos
    @property
    def intentos(self):
        return self._intentos
    def registrar_intento(self):
        self._intentos += 1
    
    def __str__(self):
        return f"{self.grado}_{self.energia}"