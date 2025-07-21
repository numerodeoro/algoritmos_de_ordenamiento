def catSort_table(lista, indice):
    """
    Ordena una lista de listas agrupando los elementos por categoría según el índice requerido,
    respetando el orden de aparición de las categorías.

    Parameters
    ----------
    lista : list of lists of int, float, str, or mixed
        Lista de listas que puede contener números, cadenas de texto o ambos en cada sublista.
        Cada elemento del índice especificado será tratado como cadena de texto para fines de agrupación.
    
    indice : int
        Posición (índice) de la columna que se utilizará para agrupar los elementos.

    Returns
    -------
    dict
        Diccionario con tres claves:
        - "categorias": lista de las categorías normalizadas encontradas;
        - "frecuencias": lista con la cantidad de veces que aparece cada categoría;
        - "ordenada": lista de listas reordenada según las categorías.

    Notes
    -----
    Todos los elementos en la posición `indice` se convierten a texto (string), se normalizan a mayúsculas
    y se eliminan espacios en blanco iniciales y finales.

    La función no modifica la lista original.

    Esta función es sensible a tildes, signos y caracteres especiales.

    Examples
    --------
    >>> lista = [
    ...     ["A", 2, "Carla"],
    ...     ["B", 1, "diego"],
    ...     ["A", 3, "Santiago"],
    ...     ["C", 2, "Sofia"],
    ...     ["B", 4, "Quique"],
    ...     ["A", 2, "Rocio"]
    ... ]
    >>> resultado = catSort2(lista, 0)
    >>> resultado["categorias"]
    ['A', 'B', 'C']
    >>> resultado["frecuencias"]
    [3, 2, 1]
    >>> resultado["ordenada"]
    [['A', 2, 'Carla'],
     ['A', 3, 'Santiago'],
     ['A', 2, 'Rocio'],
     ['B', 1, 'diego'],
     ['B', 4, 'Quique'],
     ['C', 2, 'Sofia']]
    """
    categorias=[]
    sublistas=[]
    frecuencias=[]
    for fila in lista:
        cat=str(fila[indice]).strip().upper()
        if cat in categorias:
            x=categorias.index(cat)
            frecuencias[x]=frecuencias[x]+1
            sublistas[x].append(fila)
        else:
            categorias.append(cat)
            frecuencias.append(1)
            x=categorias.index(cat)
            sublistas.append([fila])
    return {
    "categorias": categorias,
    "frecuencias": frecuencias,
    "ordenada": [fila for grupo in sublistas for fila in grupo]
}