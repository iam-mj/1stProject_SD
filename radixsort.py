#il implementam in baza 10 initial ca na atat se poate
def radix(lista, n, nmax):
    for i in range(1, len(str(nmax)) + 1): # in functie de a cata cifra de la final facem ordonarea
        aux = [0 for j in range(n)] #lista in care sortam numerele
        fr = [0 for i in range(10)] #lista in care pastram frecventele
        p = 10 ** (i - 1) #puterea la 10 la care urmeaza sa impartim pt a obtine usor cifra necesara
        for j in range(n):
            cif = (lista[j] // p) % 10
            fr[cif] += 1
        #actualizam fr astfel incat sa ne dea pozitiile elementelor in aux
        for j in range(10):
            if j == 0:
                fr[j] += -1
            else:
                fr[j] += fr[j - 1]
        #punem elementele in aux
        for j in range(n - 1, -1, -1):
            cif = (lista[j] // p) % 10
            aux[fr[cif]] = lista[j]
            fr[cif] -= 1
        #punem elementele din aux inapoi in lista in ordinea corecta
        for j in range(n):
            lista[j] = aux[j]
    return lista
