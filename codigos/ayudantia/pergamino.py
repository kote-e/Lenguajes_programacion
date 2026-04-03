class Heroe:
    def __init__(self, nombre, clase, fuerza, agilidad):
        self.nombre = nombre
        self.clase = clase
        self.fuerza = fuerza
        self.agilidad = agilidad
        
    def __repr__(self):
        return f"{self.nombre} ({self.clase}) - F:{self.fuerza} A:{self.agilidad}"
    
    def crear(self, nombre, clase, fuerza, agilidad):
        self.nombre = nombre
        self.clase = clase
        self.fuerza = fuerza
        self.agilidad = agilidad
    

# La lista de reclutas del gremio
reclutas = [
Heroe("Arthur", "Guerrero", 85, 40),
Heroe("Merlín", "Mago", 20, 30),
Heroe("Lira", "Pícara", 45, 95),
Heroe("Grom", "Orco", 95, 20),
Heroe("Elora", "Mago", 25, 60)
]