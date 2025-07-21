# archivo: catSort_flat.py
# autor: María Marta Torres
# descripción: algoritmo inventado por la autora. Muy bueno para listas mixtas con pocos valores distintos y mucha longitud.
def catSort_flat(lista):
    """
    Ordena una lista agrupando los elementos por categoría,
    respetando el orden de aparición de las categorías en la lista original.

    Parameters
    ----------
    lista : list of int, float, str, or mixed
        Lista que puede contener números, cadenas de texto o ambos. Cada elemento será
        tratado como cadena de texto (string) para fines de agrupación.

    Returns
    -------
    list of str
        Lista de cadenas con los elementos agrupados por categoría,
        en el orden en que aparecen por primera vez.

    Notes
    -----
    Todos los elementos se convierten a cadena de texto(string), se normalizan a mayúsculas
    y se eliminan espacios en blanco iniciales y finales.

    La función no modifica la lista original, pero internamente convierte
    todos los elementos a texto.

    Esta función es sensible a tildes, signos y caracteres especiales.

    Es muy útil para listas mixtas y es eficiente aún con listas largas.

    Examples
    --------
    >>> lista = [2, "hola", 2, "A", 1, 1, "*", "HOla", "a"]
    >>> catSort(lista)
    ['2', '2', 'HOLA', 'HOLA', 'A', 'A', '1', '1', '*']
    """
    lista = [str(el).strip().upper() for el in lista]
    categorias=[]
    frecuencias=[]
    catSortedList =[]
    for i, valor in enumerate(lista):
        if valor in categorias:
            x=categorias.index(valor)
            frecuencias[x]=frecuencias[x]+1
        else:
            categorias.append(valor)
            frecuencias.append(1)
    for i, frecuencia in enumerate(frecuencias):
        catSortedList.extend([categorias[i]]*frecuencia)
    return(catSortedList)