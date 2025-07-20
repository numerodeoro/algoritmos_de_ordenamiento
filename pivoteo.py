# from generador_listas import generar_lista_aleatoria, generar_lista_casi_ordenada
# from tester import test_eficiencia
    
def pivotear(lista):
    if len(lista)<=1:
        return lista
    pivote = sum(lista)/len(lista)
    mayorante=[]
    minorante=[]
    centro=[]
      
    for i in range(len(lista)):
        if lista[i]<pivote:
            minorante.append(lista[i])
        elif lista[i]>pivote:
            mayorante.append(lista[i])
        else:
            centro.append(lista[i])
    return pivotear(minorante) + centro + pivotear(mayorante)

# lista_aleatoria = generar_lista_aleatoria(100000,0,20)
# lista_casi_ordenada = generar_lista_casi_ordenada(100000,30)
# test_eficiencia(pivotear, lista_aleatoria, lista_casi_ordenada)

