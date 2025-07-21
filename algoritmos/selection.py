
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



