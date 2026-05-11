import json
from Ruta import Ruta
from Escalador import Escalador

with open('rutas.json', 'r') as file1:
    rutas_json = json.load(file1)

rutas = [Ruta(r['grado'], r['energia'], r['tecnica'], r['fuerza']) for r in rutas_json]

# BONUS
promedio_energia = sum(list(map(lambda r: r.energia, rutas))) / len(rutas)
print(promedio_energia)

escaladores = [
    Escalador("Carlos Lechuga", 40, 55, 55),
    Escalador("Valentina Palito", 53, 59, 59),
    Escalador("Gonzalo Chan", 61, 74, 62),
    Escalador("Sofia Dulce", 78, 60, 80),
    Escalador("Sebastian Titan", 84, 59, 81)
]

for escalador in escaladores:
    for ruta in rutas:
        if escalador.energia >= ruta.energia:
            if escalador.tecnica >= ruta.tecnica + 5:
                diferencia_tecnica = escalador.tecnica - ruta.tecnica
                nivel_tecnica = diferencia_tecnica // 5
                escalador.energia -= ruta.energia * (0.8 - (0.05 * nivel_tecnica))

            elif escalador.tecnica >= ruta.tecnica:
                escalador.energia -= ruta.energia

            if escalador.fuerza >= ruta.fuerza + 15:
                escalador.energia += 3

            escalador.grado_mas_dificil = ruta.grado
            escalador.contador_rutas += 1
        else: 
            break

    print(f"{escalador} escalo {escalador.contador_rutas} rutas y el grado mas dificil que escalo fue un {escalador.grado_mas_dificil}")