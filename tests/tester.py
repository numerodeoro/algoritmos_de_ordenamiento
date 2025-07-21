# tester.py
# Autor: María Marta Torres
# Banco de pruebas para algoritmos de ordenamiento: mide eficiencia en listas aleatorias y casi ordenadas.
import time
from algoritmos.bubble import bubble
from algoritmos.catSort_flat import catSort_flat
from algoritmos.insertion import ordenar
from algoritmos.selection import selec_sort
from algoritmos.pivoteo import pivotear
from utils.generador_listas import generar_lista_aleatoria, generar_lista_casi_ordenada

def test_eficiencia(algoritmo,lista):
    inicio = time.time()
    algoritmo(lista.copy())
    fin = time.time()
    tiempo = fin - inicio
    return tiempo
def tester(algoritmos=[sorted],
    min_long=10000,
    max_long=1000000, 
    inc_long = 495000, 
    min_desorden=0.1,
    max_desorden=0.7,
    inc_desorden=0.3,
    min_cat=5,
    max_cat=25,
    inc_cat=20,
    semilla=100, 
    decimales=5):
    import csv
    longitudes=[]
    longitud=min_long
    while longitud<=max_long:
        longitudes.append(longitud)
        longitud+=inc_long
        
    desordenes=[]
    desorden=min_desorden
    while desorden<=max_desorden:
        desordenes.append(desorden)
        desorden+=inc_desorden
        
    categorias=[]
    categ=min_cat
    while categ<=max_cat:
        categorias.append(categ)
        categ+=inc_cat
        
    listas=[]
    parametros=[]
    for longitud in longitudes:
        for categ in categorias:
            lista=generar_lista_aleatoria(longitud,0,categ,semilla)
            listas.append(lista)
            parametros.append([longitud,0,categ,semilla])
        for desorden in desordenes:
            lista=generar_lista_casi_ordenada(longitud,int(desorden*longitud),semilla)
            listas.append(lista)
            parametros.append([longitud,int(desorden*longitud),semilla])
    with open('resultados_tester.csv', 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['Semilla','Algoritmo', 'Tipo de lista', 'Longitud', 'Categorías o Proporción desorden', 'Tiempo'])
    
        for algoritmo in algoritmos:
            for lista, param in zip(listas, parametros):
                tiempo = test_eficiencia(algoritmo, lista)
                if len(param) == 4:
                    writer.writerow([semilla, algoritmo.__name__, 'Aleatoria', param[0], param[2], round(tiempo,decimales)])
                elif len(param) == 3:
                    writer.writerow([semilla,algoritmo.__name__, 'Casi ordenada', param[0], param[1]/param[0], round(tiempo,decimales)])

