
    
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


