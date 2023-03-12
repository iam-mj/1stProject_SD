def shell(lista, n, nmax):
    dif =  n // 2
    while dif >= 1:
        for cont in range(0, dif):
            for i in range(cont, n, dif): #trecem prin vector la distanta de dif
                j = i + dif # urmatorul el la distanta de dif
                if j < n and lista[i] > lista[j]:
                    lista[i], lista[j] = lista[j], lista[i] #daca e mai mare le inversam
                    k = i - dif #predecesorul (la distanta de dif)
                    while lista[k] > lista[i] and k > 0: # verificam daca e in ordine cu cele dinainte
                        lista[i], lista[k] = lista[k], lista[i]
                        i = k
                        k = i - dif
        dif = dif // 2
    return lista
