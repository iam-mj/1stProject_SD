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


def mediana(lista, st):
    l = []
    for i in range(5):
        l.append(lista[st + i])
    l.sort()
    return l[2]
    

def quick(lista, st, dr):
    if st < dr:
        p = lista[st]
        if st + 3 < dr:
            p = mediana(lista, st)
        vs = []
        vd = []
        pivoti = 0
        for i in range(st, dr + 1):
            if lista[i] < p:
                vs.append(lista[i])
            else:
                if lista[i] == p:
                    pivoti += 1
                if lista[i] > p:
                    vd.append(lista[i])
        
        lista1 = quick(vs, 0, len(vs) - 1)
        lista2 = quick(vd, 0, len(vd) - 1)

        lista1.extend([p for i in range(pivoti)])
        lista1.extend(lista2)

        return lista1
    else:
        return lista
