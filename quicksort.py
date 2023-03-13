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
