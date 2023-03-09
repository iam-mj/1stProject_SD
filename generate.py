import random

def gen(n, nmax):
    lista = []

    for i in range(n):
        lista.append(random.randint(0, nmax - 1))

    return lista