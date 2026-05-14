import json
from Ruta import Ruta
from Escalador import EscaladorAficionado, EscaladorElite


rutas = []
with open("rutas.json", "r") as f:
    rutas_json = json.load(f)
for ruta in rutas_json:
    rutas.append(Ruta(ruta["grado"], ruta["tecnica"], ruta["fuerza"], ruta["energia"]))

escaladores= [
    {"nombre": "Pedro Roca", "tipo": "Aficionado", "energia": 40, "tecnica": 48, "fuerza": 44, "extra": 6},
    {"nombre": "Luisa Vertical", "tipo": "Aficionado", "energia": 55, "tecnica": 62, "fuerza": 51, "extra": 8},
    {"nombre": "Marco Cima", "tipo": "Elite", "energia": 61, "tecnica": 74, "fuerza": 62, "extra": "tecnica, 3"},
    {"nombre": "Diana Cumbre", "tipo": "Elite", "energia": 78, "tecnica": 60, "fuerza": 80, "extra": "fuerza, 5"},
    {"nombre": "Rafael Tope", "tipo": "Elite", "energia": 84, "tecnica": 59, "fuerza": 81, "extra": "fuerza, 4"}]

escaladores_objetos = []
for escalador in escaladores:
    if escalador["tipo"] == "Aficionado":
        escaladores_objetos.append(EscaladorAficionado(escalador["nombre"], escalador["tecnica"], escalador["fuerza"], escalador["energia"], escalador["extra"]))
    elif escalador["tipo"] == "Elite":
        escaladores_objetos.append(EscaladorElite(escalador["nombre"], escalador["tecnica"], escalador["fuerza"], escalador["energia"], escalador["extra"]))


for escalador in escaladores_objetos:
    print(f"\033[1;36m escalador: {escalador}\033[0m")
    contador=0
    while contador < len(rutas) and escalador.puede_intentar(rutas[contador]):
        escalador.escalando(rutas[contador])
        print(f"  - {rutas[contador]}")
        contador += 1
    print(f" \033[1;35m estadisticas: \033[0m{escalador.contador_rutas} rutas escaladas, energia restante: {escalador.energia:.2f}, grado más difícil: {escalador.grado_mas_dificil} \n")