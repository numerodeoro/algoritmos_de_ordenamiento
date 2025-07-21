# archivo: bubble.py
# autor: María Marta Torres
# descripción: implementación del algoritmo de ordenamiento burbuja
def bubble(lista):
    orden = False
    while not orden:
        orden = True
        for i in range(len(lista)-1):
            if lista[i+1]<lista[i]:
                lista[i+1],lista[i]=lista[i],lista[i+1]
                orden = False
    return(lista)


    