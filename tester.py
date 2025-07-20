import time
from bubble import bubble
from catSort_flat import catSort_flat
from insertion import ordenar
from selection import selec_sort
from pivoteo import pivotear
from generador_listas import generar_lista_aleatoria, generar_lista_casi_ordenada
lista1=generar_lista_aleatoria(100000,0,20)
lista2=generar_lista_aleatoria(10000,0,20)
lista3=generar_lista_aleatoria(100000,0,100000)
lista4=generar_lista_aleatoria(10000,0,10000)
lista5=generar_lista_casi_ordenada(100000,100)
lista6=generar_lista_casi_ordenada(10000,10)
algoritmos=[catSort_flat, ordenar, selec_sort, pivotear]

def test_eficiencia(algoritmo):

    # Medición en lista aleatoria larga de pocos valores
    inicio1 = time.time()
    algoritmo(lista1.copy())
    fin1 = time.time()
    tiempo1 = fin1 - inicio1
    # Medición en lista aleatoria corta de pocos valores
    inicio2 = time.time()
    algoritmo(lista2.copy())
    fin2 = time.time()
    tiempo2 = fin2 - inicio2
    # Medición en lista aleatoria larga de muchos valores
    inicio3 = time.time()
    algoritmo(lista3.copy())
    fin3 = time.time()
    tiempo3 = fin3 - inicio3
    # Medición en lista aleatoria corta de muchos valores
    inicio4 = time.time()
    algoritmo(lista4.copy())
    fin4 = time.time()
    tiempo4 = fin4 - inicio4

    # Medición en lista casi ordenada larga
    inicio5 = time.time()
    algoritmo(lista5.copy())
    fin5 = time.time()
    tiempo5 = fin5 - inicio5

    # Medición en lista casi ordenada corta
    inicio6 = time.time()
    algoritmo(lista6.copy())
    fin6 = time.time()
    tiempo6 = fin6 - inicio6

    print(f"📊 Resultados para el algoritmo '{algoritmo.__name__}':")
    print(f" - Lista aleatoria de 100000 elementos y 20 valores: {tiempo1:.4f} segundos")
    print(f" - Lista aleatoria de 10000 elementos 20 valores: {tiempo2:.4f} segundos")
    print(f" - Lista aleatoria de 100000 elementos y 100000 valores: {tiempo3:.4f} segundos")
    print(f" - Lista aleatoria de 10000 elementos 10000 valores: {tiempo4:.4f} segundos")
    print(f" - Lista casi ordenada de 100000 elementos:   {tiempo5:.4f} segundos")
    print(f" - Lista casi ordenada de 10000 elementos:   {tiempo6:.4f} segundos")

for algoritmo in algoritmos:
    test_eficiencia(algoritmo)
