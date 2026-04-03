#importaciones necesarias
import json
from random import choice, randint, sample  
from tortuga import Tortuga

# solo para pñoner colores en la terminal :3
from colorama import Fore, Style, init
init()


# sacar los nombres de las tortugas del archivo json
with open("nombres_tortugas.json", "r") as f:
    nombres_tortugas = json.load(f)

tortugas = []
todas = nombres_tortugas["tortugas"]
seleccionados= sample(todas, 10)
#print(tortugas)

for t in seleccionados:
    tortuga = Tortuga()
    tortuga.crear_tortuga(t["nombre"], randint(1, 10), t["frase"])
    tortugas.append(tortuga)

print(f"las tortugas que correran son:")
for t in tortugas:
    print(Style.BRIGHT + Fore.MAGENTA + f"- "+ Style.RESET_ALL + f"{t.nombre}")
    

#sistema de apuesta
dinero_total= int(input("¿Cuánto dinero tienes para apostar?: "))

elegida= input("¿En qué tortuga quieres apostar?: ")
while elegida not in [t.nombre for t in tortugas]:
    print("Tortuga no válida. Por favor, elige una tortuga de la lista.")
    elegida = input("¿En qué tortuga quieres apostar?: ")

apuesta = int(input("¿Cuánto quieres apostar en esta carrera?: "))
while apuesta > dinero_total:
    print("No tienes suficiente dinero para esa apuesta. Por favor, ingresa una cantidad válida.")
    apuesta = int(input("¿Cuánto quieres apostar en esta carrera?: "))

#carrera

#ganaores
ganador= choice(tortugas)
print(f"¡La carrera ha terminado! El ganador es: {ganador.nombre}")
print(Style.BRIGHT + Fore.YELLOW + f"{ganador.nombre}: "+ Style.RESET_ALL + f"{ganador.frase}" )
if ganador == apuesta:
    print(Style.BRIGHT + Fore.GREEN+ f"¡Felicidades! {elegida} ha ganado. Tu nueva cantidad de dinero es: {dinero_total + apuesta}" + Style.RESET_ALL)
else:
    print(Style.BRIGHT + Fore.RED + f"Lo siento, {elegida} no ha ganado. Tu nueva cantidad de dinero es: {dinero_total - apuesta}" + Style.RESET_ALL)