from quicksort import quick
from countsort import count
from mergesort import merge

def select(lista, n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

def bucket(lista, n, nmax):
    #pentru mai putin de 64 de elemente intr-un bucket folosim selection sort
    if n <= 2 ** 8:
        return select(lista, n)
    else:
        #alegem numarul de buckets
        nr = 32
        buckets = [[] for i in range(nr)]
        maxs = [0 for i in range(nr)]
        #punem numerele in buckets-urile potrivite
        extra = 1
        if nmax % 32 == 0:
            extra = 0
        for i in range(n):
            key = lista[i] // ((nmax >> 5) + extra) #cand shiftam biti facem impartirea intreaga
            if key == nr: #in cazul in care dam de maxim
                key = nr - 1
            buckets[key].append(lista[i])
            if(lista[i] > maxs[key]):
                maxs[key] = lista[i]
        lista = []
        #sortam buckets-urile
        for i in range(nr):
            if maxs[i] <= 10 ** 6:
                bucket_sortat = count(buckets[i], len(buckets[i]), maxs[i])
            else:
                bucket_sortat = merge(buckets[i], len(buckets[i]), maxs[i])
            lista.extend(bucket_sortat)
        return lista