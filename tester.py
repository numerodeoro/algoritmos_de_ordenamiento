# tester.py
# Autor: María Marta Torres
# Banco de pruebas para algoritmos de ordenamiento: mide eficiencia en listas aleatorias y casi ordenadas.
import time
import csv
import os
from datetime import datetime
from algoritmos.bubble import bubble
from algoritmos.catSort_flat import catSort_flat
from algoritmos.insertion import ordenar
from algoritmos.selection import selec_sort
from algoritmos.pivoteo import pivotear
from algoritmos.dividir_unir import dividir_unir
from algoritmos.encimar import ordenar_cimas
from utils.generador_listas import generar_lista_aleatoria, generar_lista_casi_ordenada

def test_eficiencia(algoritmo,lista):
    inicio = time.time()
    algoritmo(lista.copy())
    fin = time.time()
    tiempo = fin - inicio
    return tiempo

def custom_round(numero, decimales):
    redondeado = round(numero, decimales)
    if redondeado == 0 and numero!= 0:
        return round(10 ** (-decimales),decimales)
    return redondeado

def tester(algoritmos=[sorted],
    min_long=10000,
    max_long=1000000, 
    inc_long = 495000, 
    min_desorden=10,
    max_desorden=70,
    inc_desorden=30,
    min_cat=5,
    max_cat=25,
    inc_cat=20,
    semilla=100, 
    decimales=5):
    
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
            lista=generar_lista_casi_ordenada(longitud,int(desorden/100*longitud),semilla)
            listas.append(lista)
            parametros.append([longitud,int(desorden/100*longitud),semilla])

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    nombre_archivo = f"resultados_tester_semilla{semilla}_{timestamp}.csv"
    carpeta_resultados = os.path.join(os.getcwd(), "resultados")
    os.makedirs(carpeta_resultados, exist_ok=True) 

    ruta_archivo = os.path.join(carpeta_resultados, nombre_archivo)

    with open(ruta_archivo, 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['Semilla','Algoritmo', 'Tipo de lista', 'Longitud', 'Categorías o Proporción desorden', 'Tiempo'])
    
        for algoritmo in algoritmos:
            print(f"resultados para el algoritmo: {algoritmo.__name__}\n")
            print("---------------------------------------")
            for lista, param in zip(listas, parametros):
                tiempo = test_eficiencia(algoritmo, lista)
                if len(param) == 4:
                    print(f"\ntiempo en lista aleatoria de longitud {param[0]} y cantidad de categorias {param[2]}: {custom_round(tiempo,decimales)}")
                    writer.writerow([semilla, algoritmo.__name__, 'Aleatoria', param[0], param[2], custom_round(tiempo,decimales)])
                elif len(param) == 3:
                    print(f"\ntiempo en lista casi ordenada de longitud {param[0]} y proporcion de desorden {int(param[1]/param[0]*100)}: {custom_round(tiempo,decimales)}")
                    writer.writerow([semilla,algoritmo.__name__, 'Casi ordenada', param[0], int(param[1]/param[0]*100), custom_round(tiempo,decimales)])

tester(algoritmos=[catSort_flat ,dividir_unir],
    min_long=100,
    max_long=1100,
    inc_long = 100,
    min_desorden=10,
    max_desorden=90,
    inc_desorden=10,
    min_cat=5,
    max_cat=15,
    inc_cat=5,
    semilla=576,
    decimales=5)