n = 0
lista = []

def citire():
    global n, lista
    file_name = input("Dati numele fisierului test: ")
    f = open(file_name);
    n = int(f.readline().strip())
    lista = [int(x) for x in f.readline().split()]
    f.close()

def afisare():
    global n, lista
    file_out = input("Dati fisierul de output: ")
    g = open(file_out, "w")
    for i in range(n):
        g.write(str(lista[i]) + ' ')
    g.close()

def interclasare(lista1, lista2):
    l1 = len(lista1) - 1
    l2 = len(lista2) - 1
    rez = []
    i = 0
    j = 0
    while i <= l1 and j <= l2:
        if lista1[i] < lista2[j]:
            rez.append(lista1[i])
            i += 1
        else:
            rez.append(lista2[j])
            j += 1
    while i <= l1:
        rez.append(lista1[i])
        i += 1
    while j <= l2:
        rez.append(lista2[j])
        j += 1
    return rez

def merge(lista, st, dr):
    if st < dr:
        mij = (st + dr) // 2
        rez = interclasare(merge(lista, st, mij), merge(lista, mij + 1, dr))
        return rez
    else:
        return [lista[st]]
