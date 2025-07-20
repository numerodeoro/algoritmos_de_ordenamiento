# import time
# import random
# random.seed(100)
# lista=[]
# for i in range(10000):
#     lista.append(random.randint(0,20))
# lista_casi_ordenada = list(range(10000))
# # Introducimos un pequeño desorden: intercambiamos 10 pares aleatorios
# for _ in range(10):
#     i = random.randint(0, 9999)
#     j = random.randint(0, 9999)
#     lista_casi_ordenada[i], lista_casi_ordenada[j] = lista_casi_ordenada[j], lista_casi_ordenada[i]
def ordenar(lista):
    for i in range(1,len(lista)):
        aux=lista[i]
        j=i-1
        while j>=0 and lista[j]>aux:
            lista[j+1]=lista[j]
            j=j-1
        lista[j+1]=aux
    return(lista)

# inicio=time.time()
# sorted_lista = ordenar(lista_casi_ordenada.copy())
# fin=time.time()
# print(f"tiempo de ejecucion: {fin-inicio}")
# x = [45,23,65,789,1,0,78]
# sorted_x=ordenar(x.copy())
# print(f"la lista ordenada es: {sorted_x}")
# print(f"la lista original es: {x}")