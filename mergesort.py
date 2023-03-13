def interclasare(lista1, lista2):
    l1 = len(lista1) - 1
    l2 = len(lista2) - 1
    rez = []
    i = 0
    j = 0
    while i <= l1 and j <= l2:
        if lista1[i] < lista2[j]:
            rez.append(lista1[i])
            i += 1
        else:
            rez.append(lista2[j])
            j += 1
    while i <= l1:
        rez.append(lista1[i])
        i += 1
    while j <= l2:
        rez.append(lista2[j])
        j += 1
    return rez

def merge(lista, n, nmax):
    return mergesort(lista, 0, n - 1)

def mergesort(lista, st, dr):
    if st < dr:
        mij = (st + dr) // 2
        rez = interclasare(mergesort(lista, st, mij), mergesort(lista, mij + 1, dr))
        return rez
    else:
        return [lista[st]]
