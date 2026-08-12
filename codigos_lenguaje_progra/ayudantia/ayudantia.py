class Guardian:
    def __init__(self, nombre, nivel):
        self.nombre= nombre
        self.nivel= nivel
        
    def presentarse(self):
        return f" {self.nombre}, guardian del nivel {self.nivel}"
    
    def accion_principal(self):
        return f"el guardian se mantiene en guardia."
    

class Guerrero(Guardian):
    def __init__(self, nombre, nivel, fuerza):
        super().__init__(nombre, nivel)
        self.fuerza= fuerza
    
    def presentarse(self):
        return f"Soy el guerrero {super().presentarse()} con fuerza {self.fuerza}"
    
    def accion_principal(self):
        return f"El guerrero ataca con su espada!"
    

class Mago(Guardian):
    def __init__(self, nombre, nivel, mana):
        super().__init__(nombre, nivel)
        self.mana= mana
    
    def presentarse(self):
        return f"Soy {self.nombre}, un mago de nivel {self.nivel} con {self.mana} de poder mágico"
    
        

ejercito= [Guerrero("juan", 2, 20), Mago("frieren", 20, 1000)]
for i in ejercito:
    print(f"{i.accion_principal()}")