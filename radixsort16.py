#il implementam in baza 10 initial ca na atat se poate
#il implementam si in baza 16 dar momentan atat
'''
n = 0
lista = []
nmax = 0

def citire():
    global n, nmax, lista
    n, nmax = [int(x) for x in input("Dati n si nmax: ").split()]
    lista = [int(x) for x in input("Dati lista: ").split()]

def afisare():
    global n, lista
    print(*lista)
'''

#functia de transformare in alta baza
def transf16(element):
    list = []
    while element:
        list.append(element % 16)
        element = element >> 4
    list = list[::-1]
    return list

#functia de transformare inapoi in baza 10
def transf10(list, p): #alegem baza de forma 2 ** p
    el = 0
    for i in range(len(list)):
        el = el << p + list[i]
    return el

def radix16(lista, n, nmax):
    imax = 0
    b = 16
    p = 4
    for i in range(len(lista)):
        if lista[i] == nmax:
            imax = i
        lista[i] = transf16(lista[i])
        #fiecare element are intr-o lista "cifrele" din care e format in baza respectiva 
    for i in range(1, len(lista[imax]) + 1): # in functie de a cata cifra de la final facem ordonarea
        aux = [0 for j in range(n)]
        fr = [0 for j in range(b)]
        for j in range(n):
            cif = 0
            l = len(lista[j])
            if l - i + 1 > 0:
                cif = lista[j][l - i]
            fr[cif] += 1 #crestem frecventa acordingly
        for j in range(b): #modificam vectorul de frecventa pt a ne da pozitiile
            if j == 0:
                fr[j] += -1
            else:
                fr[j] += fr[j - 1]
        for j in range(n - 1, -1, -1): #pui in aux val conform pozitiilor din fr[]
            cif = 0
            l = len(lista[j])
            if l - i + 1 > 0:
                cif = lista[j][l - i]
            aux[fr[cif]] = lista[j]
            fr[cif] -= 1
        #punem val din aux in lista
        for j in range(n):
            lista[j] = aux[j]
    
    for i in range(n):
        lista[i] = transf10(lista[i], p)

    return lista
    