def mediana(lista):
    l = []
    for i in range(5):
        l.append(lista[i])
    l.sort()
    return l[2]


def quicksort(lista, n):
    if n > 1:
        p = lista[0]
        if n > 4:
            p = mediana(lista)
        vs = []
        vd = []
        pivoti = 0
        for i in range(n):
            if lista[i] < p:
                vs.append(lista[i])
            else:
                if lista[i] == p:
                    pivoti += 1
                else:
                    vd.append(lista[i])
        
        lista1 = quicksort(vs, len(vs))
        lista2 = quicksort(vd, len(vd))

        lista1 += [p for i in range(pivoti)]
        lista1 += lista2

        return lista1
    else:
        return lista


def quick(lista, n, nmax):
    return quicksort(lista, n)


'''
def quicksort(lista, st, dr):
    if st < dr:
        p = lista[st]
        if st + 3 < dr:
            p = mediana(lista, st)
        vs = []
        vd = []
        pivoti = 0
        for i in range(st, dr + 1):
            if lista[i] < p:
                vs.append(lista[i])
            else:
                if lista[i] == p:
                    pivoti += 1
                if lista[i] > p:
                    vd.append(lista[i])
        
        lista1 = quicksort2(vs, 0, len(vs) - 1)
        lista2 = quicksort2(vd, 0, len(vd) - 1)

        lista1.extend([p for i in range(pivoti)])
        lista1.extend(lista2)

        return lista1
    else:
        return lista


def quicksort2(lista, st, dr):
    return quicksort(lista, st, dr)
'''