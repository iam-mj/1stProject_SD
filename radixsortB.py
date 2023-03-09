#il implementam in baza 10 initial ca na atat se poate
#il implementam si in bazele 2, 8 dar momentan atat
n = 0
nmax = 0
b = 0
lista = []

def citire():
    global n, b, nmax, lista
    file_name = input("Dati numele fisierului test: ")
    f = open(file_name);
    n, nmax, b = [int(x) for x in f.readline().split()]
    lista = [int(x) for x in f.readline().split()]
    f.close()

def afisare():
    global n, lista
    file_out = input("Dati fisierul de output: ")
    g = open(file_out, "w")
    for i in range(n):
        g.write(str(lista[i]) + ' ')
    g.close()

def radix():
    global n, b, nmax, lista
    for i in range(1, len(str(nmax)) + 1): # in functie de a cata cifra de la final facem ordonarea
        aux = [0 for j in range(n)]
        fr = [0 for j in range(b)]
        for j in range(n):
            cif = 0
            l = len(str(lista[j]))
            if l - i + 1 > 0:
                cif = int(str(lista[j])[l - i])
            fr[cif] += 1 #crestem frecventa acordingly
        for j in range(b): #modificam vectorul de frecventa pt a ne da pozitiile
            if j == 0:
                fr[j] += -1
            else:
                fr[j] += fr[j - 1]
        for j in range(n - 1, -1, -1): #pui in aux val conform pozitiilor din fr[]
            cif = 0
            l = len(str(lista[j]))
            if l - i + 1 > 0:
                cif = int(str(lista[j])[l - i])
            aux[fr[cif]] = lista[j]
            fr[cif] -= 1
        #punem val din aux in lista
        for j in range(n):
            lista[j] = aux[j]

citire()
radix()
afisare()