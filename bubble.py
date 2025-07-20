
# from generador_listas import generar_lista_aleatoria, generar_lista_casi_ordenada
# from tester import test_eficiencia
def bubble(lista):
    orden = False
    while not orden:
        orden = True
        for i in range(len(lista)-1):
            if lista[i+1]<lista[i]:
                lista[i+1],lista[i]=lista[i],lista[i+1]
                orden = False
    return(lista)
# lista_aleatoria = generar_lista_aleatoria()
# lista_casi_ordenada = generar_lista_casi_ordenada()
# test_eficiencia(bubble, lista_aleatoria, lista_casi_ordenada)

    