from pergamino import Heroe

heroes=[]

reclutas = [
["Arthur", "Guerrero", 85, 40],
["Merlín", "Mago", 20, 30],
["Lira", "Pícara", 45, 95],
["Grom", "Orco", 95, 20],
["Elora", "Mago", 25, 60]
]
for i in reclutas:
    h= Heroe(i[0], i[1], i[2], i[3])
    heroes.append(h)
#print(heroes)
    

#fuersa
nuevalista=sorted(heroes, key=lambda heroe: heroe.fuerza, reverse=True )
print(f"los heroes son: {nuevalista}")

#dragon
equipo_sigilo= list(filter(lambda x: (x.agilidad > 50), heroes))
print(equipo_sigilo)


with open("registro_nombres.txt", "w") as file:
    nombres=list(map(lambda x: f" {x.nombre} el {x.clase}", heroes))
    for i in nombres:
        file.write(f" {i}\n")

alfabeticamente=sorted(sorted(heroes, key=lambda y: y.agilidad, reverse=True), key=lambda x: x.clase)
print(alfabeticamente)


feuerte=max(heroes, key=lambda z: z.fuerza + z.agilidad)
print(feuerte)
