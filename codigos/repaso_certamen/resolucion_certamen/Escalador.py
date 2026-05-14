from Ruta import Ruta

class Escalador:
    def __init__(self, nombre, tecnica, fuerza, energia):
        self.nombre = nombre
        self.tecnica = tecnica
        self.fuerza = fuerza
        
        self.contador_rutas = 0
        self.grado_mas_dificil = None
        
        self._energia = energia
  
    @property
    def energia(self):
        return self._energia
    @energia.setter
    def energia(self, valor):
        if valor <0:
            self._energia = 0
        else:
            self._energia = valor
    
    def __str__(self):
        return f"{self.nombre}"
    
    def __repr__(self):
        return f"{self.nombre} - {self.tecnica} - {self.fuerza} - {self.energia:.2f}"
    
    

class EscaladorAficionado(Escalador):
    def __init__(self, nombre, tecnica, fuerza, energia, limite_rutas):
        super().__init__(nombre, tecnica, fuerza, energia)
        self.limite_rutas = limite_rutas
    
    def puede_intentar(self, ruta):
        if self._energia >= ruta.energia and self.contador_rutas < self.limite_rutas:
            return True
        else:
            return False

    def escalando(self, ruta):
        if self.puede_intentar(ruta):
            self.contador_rutas += 1
            self.energia -= (ruta.energia * 1.1)
            grado = ruta.grado
            self.grado_mas_dificil = grado
            

    def __str__(self):
        return f"{super().__str__()} (maximo {self.limite_rutas} rutas)"

class EscaladorElite(Escalador):
    def __init__(self, nombre, tecnica, fuerza, energia, especialidad):
        super().__init__(nombre, tecnica, fuerza, energia)
        self.especialidad = especialidad[:especialidad.find(",")]
        self.recuperacion= especialidad[:especialidad.find(",")]
    
    def puede_intentar(self, ruta):
        if self.energia >= ruta.energia:
            return True
        else:
            return False
    
    def escalando(self, ruta):
        if self.puede_intentar(ruta):
            self.contador_rutas += 1
            grado = ruta.grado
            self.grado_mas_dificil = grado 
            if self.especialidad == "tecnica" and self.tecnica>= ruta.tecnica+10:
                self.energia -= (ruta.energia * 0.8)
            elif self.especialidad == "fuerza" and self.fuerza >= ruta.fuerza+10:
                self.energia -= (ruta.energia * 0.85)
            else:
                self.energia -= ruta.energia
        
    def __str__(self):
        return f"{super().__str__()} [{self.especialidad}]"

