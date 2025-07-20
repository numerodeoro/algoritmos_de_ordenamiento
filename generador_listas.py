import random

random.seed(100)

def generar_lista_aleatoria(longitud=10000, minimo=0, maximo=20):
    return [random.randint(minimo, maximo) for _ in range(longitud)]

def generar_lista_casi_ordenada(longitud=10000, desordenes=10):
    lista = list(range(longitud))
    for _ in range(desordenes):
        i, j = random.randint(0, longitud-1), random.randint(0, longitud-1)
        lista[i], lista[j] = lista[j], lista[i]
    return lista
