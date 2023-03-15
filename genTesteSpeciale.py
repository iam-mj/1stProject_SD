import random
import math

#genereaza o lista de nr crescatoare
def cresc(n, nmax):
    start = random.randint(0, nmax - n)
    lista = [x for x in range(start, start + n)]

    return lista

#genereaza o lista de nr descrescatoare
def descresc(n, nmax):
    start = random.randint(n - 1, nmax - 1)
    lista = [x for x in range(start, start - n, -1)]

    return lista 

#genereaza o lista de numere aproape sortate
def aproapeSortat(n, nmax):
    start = random.randint(0, nmax - n)
    lista = [x for x in range(start, start + n)]
    #avem o lista sortata crescator

    #realizam aleatoriu cateva swap-uri
    for i in range(math.floor(math.log10(n)) * 20):
        i1 = random.randint(0, n - 1)
        i2 = random.randint(0, n - 1)
        lista[i1], lista[i2] = lista[i2], lista[i1]

    return lista

#genereaza o lista de numere apropiate
def apropiat(n, nmax):
    lista = []

    for i in range(n):
        lista.append(random.randint(nmax - 1000, nmax - 1))

    return lista

