# import time
# import random
# random.seed(100)
# lista = []
# for i in range(10000):
#     x=random.randint(0,20)
#     lista.append(x)
# lista_casi_ordenada = list(range(10000))
# # Introducimos un pequeño desorden: intercambiamos 10 pares aleatorios
# for _ in range(10):
#     i = random.randint(0, 9999)
#     j = random.randint(0, 9999)
#     lista_casi_ordenada[i], lista_casi_ordenada[j] = lista_casi_ordenada[j], lista_casi_ordenada[i]
def selec_sort(lista):
    """
    Ordena una lista en forma ascendente usando Selection Sort.

    Parameters
    ----------
    lista : list int or float
        Lista de números a ordenar.

    Returns
    -------
    list
        Lista ordenada en forma ascendente.

    Notes
    -----
    La función realiza los intercambios in place, por lo que es recomendable
    pasar como argumento una copia de la lista si querés conservar la original.

    Examples
    --------
    >>> lista = [2, 3, 6, 4]
    >>> ordenar(lista.copy())
    [2, 3, 4, 6]
    """
    for i in range(len(lista)):
        posicion = i
        for j in range(i+1,len(lista)):
            if lista[j]<lista[posicion]:
                posicion = j
        lista[i],lista[posicion]=lista[posicion],lista[i]    
    return(lista)
# inicio=time.time()
# sorted_lista = selec_sort(lista_casi_ordenada.copy())
# fin=time.time()
# print(f"tiempo de ejecucion: {fin-inicio}")
# print(f"lista original: {lista}")
# print(f"lista ordenada: {sorted_lista}")


