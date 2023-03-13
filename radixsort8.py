# 8 e de fapt infinit =))

#functia de transformare in alta baza
def transf16(element):
    list = []
    if element == 0:
        list = [0]
    while element:
        list.append(element % (1 << 16)) #element % (2 ** 16) 
        element = element >> 16
    return list #intoarce o lista cu cifrele numarului in noua baza dar de la final la inceput

#functia de transformare inapoi in baza 10
def transf10(list, p): #alegem baza de forma 2 ** p
    list = list[::-1] #numarul era stocat de la dreapta la stanga
    el = 0
    for i in range(len(list)):
        el = el << p
        el += list[i]
    return el

def radix8(lista, n, nmax):
    imax = 0
    emax = max(lista) #maximul din lista
    b = 1 << 16 #2 ** 16
    p = 16
    for i in range(len(lista)):
        if lista[i] == emax:
            imax = i
        lista[i] = transf16(lista[i])
        #fiecare element are intr-o lista "cifrele" din care e format in baza respectiva 
    for i in range(0, len(lista[imax])): 
    #in functie de a cata cifra de la final facem ordonarea (consideram ultima cifra ca fiind cifra 0)
    #numerele noastre oricum is trecute de la dreapta la stanga in lista dar anywaysss
        aux = [0 for j in range(n)]
        fr = [0 for j in range(b)]
        for j in range(n):
            cif = 0
            l = len(lista[j])#cate cifre are numarul
            if l > i:
                cif = lista[j][i]
            fr[cif] += 1 #crestem frecventa acordingly
        for j in range(b): #modificam vectorul de frecventa pt a ne da pozitiile
            if j == 0:
                fr[j] += -1 #la fr[0] scadem 1 fiindca aux e indexat de la 0
            else:
                fr[j] += fr[j - 1]
        for j in range(n - 1, -1, -1): #pui in aux val conform pozitiilor din fr[]
            cif = 0
            l = len(lista[j])
            if l > i:
                cif = lista[j][i]
            aux[fr[cif]] = lista[j]
            fr[cif] -= 1
        #punem val din aux in lista
        for j in range(n):
            lista[j] = aux[j]
    
    for i in range(n):
        lista[i] = transf10(lista[i], p)

    return lista
    