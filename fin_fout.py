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
