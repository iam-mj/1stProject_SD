def count(lista, n, nmax):
    fr = [0 for i in range(nmax + 1)]
    for x in lista:
        fr[x] += 1
    lista = []
    for i in range(nmax + 1):
        for j in range(fr[i]):
            lista.append(i)
    return lista    
