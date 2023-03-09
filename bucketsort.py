import math
from quicksort import quick
n = 0
nmax = 0
lista = []
'''
def citire():
    global n, nmax, lista
    file_name = input("Dati numele fisierului test: ")
    f = open(file_name);
    n, nmax = [int(x) for x in f.readline().split()]
    lista = [int(x) for x in f.readline().split()]
    f.close()

def afisare():
    global n, lista
    file_out = input("Dati fisierul de output: ")
    g = open(file_out, "w")
    for i in range(n):
        g.write(str(lista[i]) + ' ')
    g.close()
'''
def select(lista, n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

def count(lista, n, nmax):
    fr = [0 for i in range(nmax + 1)]
    for x in lista:
        fr[x] += 1
    k = 0
    for i in range(nmax):
        for j in range(fr[i]):
            lista[k] = i
            k += 1
    return lista

def bucket(lista, n, nmax):
    #pentru mai putin de 64 de elemente intr-un bucket folosim selection sort
    if n <= 2 ** 8:
        return select(lista, n)
    else:
        #alegem numarul de buckets
        if nmax <= 64:
            #daca avem multe nr mici folosim count
            return count(lista, n, nmax)
        else:
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
                bucket_sortat = quick(buckets[i], 0, len(buckets[i]) - 1)
                #bucket_sortat = bucket(buckets[i], len(buckets[i]), maxs[i])
                lista.extend(bucket_sortat)
            return lista

