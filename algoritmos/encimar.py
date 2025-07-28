def encimar(lista,n):
    if n>1:
        max_i=int(n/2)
        for i in range(max_i+1):
            cima = int((n-1-2*i)/2)
            izq = 2*cima+1
            der= 2*cima+2
            if der<=n-1 and izq<=n-1:
                if lista[der]>lista[cima] and lista[der]>lista[izq]:
                    lista[der],lista[cima]=lista[cima],lista[der]
                elif lista[izq]>lista[cima]and lista[izq]>=lista[der]:
                    lista[izq],lista[cima]=lista[cima],lista[izq]
            elif izq<=n-1:
                if lista[izq]>lista[cima]:
                    lista[izq],lista[cima]=lista[cima],lista[izq]

        lista[n-1],lista[0]=lista[0],lista[n-1]  
    return lista            
def ordenar_cimas(lista):
    n=len(lista)
    ordenada=lista.copy()
    for i in range(n+1):
        aux=encimar(ordenada[:n-i], n-i)
        ordenada=aux+ordenada[n-i:]
    return(ordenada)
lista=[10,8,8,23,-1,-4,3,2,8,11,9,4,0,2,1, 23,5,1,78,0,-10,31,1,1,1,1,1,0,0,0]
print(ordenar_cimas(lista))

