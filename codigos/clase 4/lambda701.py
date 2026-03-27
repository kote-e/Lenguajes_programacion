def cuadrado(z):
    return z ** 2

x = lambda y: y ** 2

c1 = cuadrado(3)
print(c1)

c2 = x(3)
print(c2)

import json 

with open("paises.json", "r") as f:
    paises = json.load(f)

# print(paises)

# nombres = list(map(lambda x: x['pais'], paises))
# copas = list(map(lambda x: x['globos_de_oro'], paises))

# print(nombres)
# print(copas)

# from matplotlib import pyplot as plt

# plt.figure(1)
# plt.bar(nombres, copas)
# plt.show()

paises = filter(lambda x: x['participaciones_mundial'] > 10, paises)
print(paises)
paises = sorted(paises, key = lambda x: x['copas_america'], reverse=True)
print(paises)

# foo = False
# bar = 20
# linea = 'x' if foo is True else 'a' if bar > 50 else 'b'
# print(linea)

