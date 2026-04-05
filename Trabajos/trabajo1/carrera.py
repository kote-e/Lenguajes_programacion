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

print(Style.BRIGHT + Fore.CYAN + f"¡Bienvenido a la carrera de tortugas!" + Style.RESET_ALL)
dinero_total= int(input("¿Cuánto dinero tienes para apostar?: ")) # para que el usuario pueda apostar, y se le vaya restando o sumando dependiendo de si gana o pierde la apuesta.
for t in seleccionados:
    tortuga = Tortuga()
    tortuga.crear_tortuga(t["nombre"], t["frase"])
    tortugas.append(tortuga)

print(f"las tortugas que correran son:")
for t in tortugas:
    print(Style.BRIGHT + Fore.MAGENTA + f"- "+ Style.RESET_ALL + f"{t.nombre}")
    

#sistema de apuesta
elegida= input("¿En qué tortuga quieres apostar?: ")
while elegida not in [t.nombre for t in tortugas]:
    print("Tortuga no válida. Por favor, elige una tortuga de la lista.")
    elegida = input("¿En qué tortuga quieres apostar?: ")

apuesta = int(input("¿Cuánto quieres apostar en esta carrera?: "))
while apuesta > dinero_total:
    print("No tienes suficiente dinero para esa apuesta. Por favor, ingresa una cantidad válida.")
    apuesta = int(input("¿Cuánto quieres apostar en esta carrera?: "))

#carrera
print(f"\n{Style.BRIGHT + Fore.CYAN}🏁 ¡Comienza la carrera! 🏁{Style.RESET_ALL}\n")


alguien_gano = False
while not alguien_gano:
    posiciones = []

    for t in tortugas:
        if t.avanza: #revisa si se catapulta o no o si tiene un mal viaje, si no tiene ninguno de esos eventos avanza normalmente
            t.velocidad = randint(1, 4)  # la tortuga avanza una distancia aleatoria basada en su velocidad
            t.distancia_recorrida += t.velocidad
            posiciones.append(t)
        else:
            t.si_no_abanza= -1
            if t.si_no_abanza <= 0:
                t.avanza= True
                
            
    posiciones.sort(key=lambda x: x.distancia_recorrida, reverse=True)
    for i in posiciones:
        i.posicion_carrera= posiciones.index(i) + 1
    
    for t in posiciones:
        #eventos aleatorios
        if randint(1, 100) <= 6:  # 6% de probabilidad de que ocurra un evento
            evento= choice(["aji", "alas", "burocracia", "catapulta", "hongo"])
            if evento == "aji":
                t.distancia_recorrida += 5
                print(Style.BRIGHT + Fore.RED + f"¡{t.nombre} comio ají potente y avanza 5 metros extra!" + Style.RESET_ALL)
            elif evento == "alas":
                if t.posicion_carrera == 1:
                    t.distancia_recorrida += 10
                    print(Style.BRIGHT + Fore.CYAN + f"¡{t.nombre} usa alas de ángel y avanza 10 metros extra!" + Style.RESET_ALL)
                else:
                    delante = delante = posiciones[t.posicion_carrera - 2]
                    if delante.posicion_carrera == t.posicion_carrera-1:
                        t.distancia_recorrida = delante.distancia_recorrida + 1
                        print(Style.BRIGHT + Fore.CYAN + f"¡{t.nombre} usa alas de ángel y adelanta a {delante.nombre}!" + Style.RESET_ALL)
                        break
            elif evento == "burocracia":
                t.distancia_recorrida -= t.velocidad
                print(Style.BRIGHT + Fore.YELLOW + f"¡{t.nombre} no avanza!" + Style.RESET_ALL)
            elif evento == "catapulta":
                t.avanza= False
                t.si_no_abanza= 3
                print(Style.BRIGHT + Fore.MAGENTA + f"¡{t.nombre} fue catapultado/a!, en 3 turnos caera 20 metros delante" + Style.RESET_ALL)
                t.distancia_recorrida += 20
            elif evento == "hongo":
                if randint(0,1)== 0:
                    t.distancia_recorrida += 40
                    print(Style.BRIGHT + Fore.GREEN + f"¡{t.nombre} comio un hongo, otiene una apertura de conciencia lo que le permite encontrar un atajo  y avanza 40 metros extra!" + Style.RESET_ALL)
                else:
                    t.avanza= False
                    t.si_no_abanza= 4
                    print(Style.BRIGHT + Fore.GREEN + f"¡{t.nombre} comio un hongo, pero no paso un buentiampo! Se desmaya y no avanza durante 4 turnos!" + Style.RESET_ALL)
                

    if posiciones[0].distancia_recorrida >= 1000:
        alguien_gano = True
        ganador = posiciones[0]



#ganaores
#ganador= choice(tortugas) # solo para confirmar que el sistema de apuestas funciona :)
print(f"¡La carrera ha terminado! El ganador es: {ganador.nombre}")
print(Style.BRIGHT + Fore.YELLOW + f"{ganador.nombre}: "+ Style.RESET_ALL + f"{ganador.frase}" )

#3 mejores
print(f"\n {Style.BRIGHT + Fore.CYAN}🏆 ¡Resultados de la carrera! 🏆{Style.RESET_ALL}\n")
for i in enumerate(posiciones[:-1]):
    if i[0] < 3:
        print(Style.BRIGHT + Fore.YELLOW + f"{i[0]+1}. "+ Style.RESET_ALL + f"{i[1].nombre} recorrio: {i[1].distancia_recorrida} metros")
    else:
        print(f"{i[0]+1}. {i[1].nombre} recorrio: {i[1].distancia_recorrida} metros")



if ganador.nombre == elegida:
    dinero_total += apuesta
    print(Style.BRIGHT + Fore.GREEN+ f"¡Felicidades! {elegida} ha ganado. Tu nueva cantidad de dinero es: {dinero_total}" + Style.RESET_ALL)
    
else:
    dinero_total -= apuesta
    print(Style.BRIGHT + Fore.RED + f"Lo siento, {elegida} no ha ganado. Tu nueva cantidad de dinero es: {dinero_total}" + Style.RESET_ALL)
    