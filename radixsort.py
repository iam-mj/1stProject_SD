#il implementam in baza 10 initial ca na atat se poate
n = 0
nmax = 0
lista = []

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

def radix(lista, n, nmax):
    for i in range(1, len(str(nmax)) + 1): # in functie de a cata cifra de la final facem ordonarea
        aux = [0 for j in range(n)]
        fr = [0 for i in range(10)]
        for j in range(n):
            cif = 0
            l = len(str(lista[j]))
            if l - i + 1 > 0:
                cif = int(str(lista[j])[l - i])
            fr[cif] += 1
        for j in range(10):
            if j == 0:
                fr[j] += -1
            else:
                fr[j] += fr[j - 1]
        for j in range(n - 1, -1, -1):
            cif = 0
            l = len(str(lista[j]))
            if l - i + 1 > 0:
                cif = int(str(lista[j])[l - i])
            aux[fr[cif]] = lista[j]
            fr[cif] -= 1
        for j in range(n):
            lista[j] = aux[j]
    return lista
