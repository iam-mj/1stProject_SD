#il implementam in baza 16
def radix4(lista, n, nmax):
    b = 16
    putere = 4 #baza e 2 ** putere
    putereActuala = 0 #p e 2 ** putereActuala
    maxim = max(lista)
    p = 1 #puterea la baza la care urmeaza sa impartim pt a obtine usor cifra necesara
    while(maxim / p >= 1):
        aux = [0 for j in range(n)] #lista in care sortam numerele
        fr = [0 for i in range(b)] #lista in care pastram frecventele
        for j in range(n):
            cif = (lista[j] >> putereActuala) & (b - 1) #& (b - 1) <=> % b
            fr[cif] += 1
        #actualizam fr astfel incat sa ne dea pozitiile elementelor in aux
        for j in range(b):
            if j == 0:
                fr[j] += -1
            else:
                fr[j] += fr[j - 1]
        #punem elementele in aux
        for j in range(n - 1, -1, -1):
            cif = (lista[j] >> putereActuala) & (b - 1)
            aux[fr[cif]] = lista[j]
            fr[cif] -= 1
        #punem elementele din aux inapoi in lista in ordinea corecta
        for j in range(n):
            lista[j] = aux[j]
        #nu uitam sa crestem p
        p = p << putere
        putereActuala += putere
    return lista
