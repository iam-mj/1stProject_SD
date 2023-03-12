#il implementam in baza 10 initial ca na atat se poate
#il implementam si in bazele 2, 8 dar momentan atat
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