# archivo: dividir_unir.py
# autor: María Marta Torres
# descripción: ordenamiento merge clásico, versión mm :D
def dividir_unir(lista):
    if len(lista) <= 1:
        return lista
    else:
        pos_centro = int(len(lista)/2)
        IZQ = dividir_unir(lista[:pos_centro])
        DER = dividir_unir(lista[pos_centro:])
        return unir(IZQ, DER)
def unir(lista1,lista2):
    unida = []
    cont1 = 0
    cont2 = 0
    while len(lista1)>=1 and len(lista2)>=1 and cont1<len(lista1) and cont2<len(lista2):
        if lista1[cont1]<=lista2[cont2]:
            unida.append(lista1[cont1])
            cont1+=1
        else:
            unida.append(lista2[cont2])
            cont2+=1
    if cont1==len(lista1) and cont2<len(lista2):
        unida=unida+lista2[cont2:]
    else:
        unida=unida+lista1[cont1:]
    return unida







