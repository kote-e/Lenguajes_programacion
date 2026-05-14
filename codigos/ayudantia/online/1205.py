class Persona:
    def __init__(self, estatura, peso, edad):
        self.estatura = estatura
        self.peso = peso
        self.edad = edad
 
    def imprimir_estatura(self):
        print(f"Mide {self.estatura:.2f} mts")
 
    def get_id(self):
        return f"{self.estatura} - {self.peso} - {self.edad}"

    def __eq__(self, value) -> bool:
        return self.get_id() == value.get_id()
 
class PersonaConNombre(Persona):
    def __init__(self, estatura, peso, edad, nombre):
        super().__init__(estatura, peso, edad)
        self.nombre = nombre

    def presentarse(self):
        print(f"Hola, que tal? Me llamo {self.nombre}")
 
    def __str__(self) -> str:
        return self.nombre
 
    def __repr__(self) -> str | int:
        return f"{self.nombre} - {self.edad} - {self.estatura:.2f}"
 
class PersonaConNombreYApellido(PersonaConNombre):

    def __init__(self, estatura, peso, edad, nombre, apellido):
        super().__init__(estatura, peso, edad, nombre)
        self.apellido = apellido
 
    def presentarse(self):
        print(f"Hola, que tal? Me llamo {self.nombre} {self.apellido}")
 
    def __str__(self) -> str:
        return self.nombre

    def __repr__(self) -> str | int:
        return f"{self.nombre} - {self.edad} - {self.estatura:.2f}"

 
 
persona = Persona(1.75, 65, 30)
 
jose_1 = PersonaConNombre(1.6945321, 65, 24, "José")

jose_2 = PersonaConNombreYApellido(1.75, 65, 30, "José", "Vidal")
 
benjamin_1 = PersonaConNombre(1.65, 70, 21, "Benjamín")

benjamin_2 = PersonaConNombre(1.75, 70, 18, "Benjamín")
 
personas = [jose_1 ,jose_2, benjamin_1, benjamin_2]
 
jose_1.presentarse()

jose_2.presentarse()

 