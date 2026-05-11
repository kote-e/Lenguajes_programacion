from random import randint

numeros_random = [randint(1,100) for i in range(10)]

[print(numeros_random)]

cuadrados = list(map(lambda x: x ** 2,numeros_random))
mayores_mil = list(filter(lambda x: x > 5000, cuadrados))
print(cuadrados)
print(mayores_mil)

