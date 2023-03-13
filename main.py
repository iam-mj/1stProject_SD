import time
from generate import gen
from mergesort import merge
from bucketsort import bucket
from quicksort import quick
from radixsort import radix
from radixsort16 import radix16
from radixsort8 import radix8
from shellsort import shell
from countsort import count

i = "1"
f = open("tests.txt")
g = open("rezultate" + i + ".txt", "w")
nr_teste = int([x for x in f.readline().split()][2])
sorts = [radix, radix16, radix8, shell, merge, bucket, count]
ch_sorts = ["radix", "radix16", "radix8", "shell", "merge", "bucket", "count"]
#teste - lista cu informatii despre testele noastre
teste = []
for i in range(nr_teste):
    test = [x for x in f.readline().split()]
    test = [int(test[i]) for i in [2, 5]]
    teste.append(test)
f.close()

teste.append([10 ** 6, 10 ** 6])

cnt = 0
for test in teste:
    cnt += 1
    #generam numerele
    lista = gen(test[0], test[1])

    g.write("\n Testul " + str(cnt) + " N = " + str(test[0]) + " Max = " + str(test[1]) + ":")
    print("\n Testul " + str(cnt) + " N = " + str(test[0]) + " Max = " + str(test[1]), end = ':')

    timp_start_py = time.time()
    lista_py = sorted(lista)
    timp_stop_py = time.time()

    g.write("\n - a durat " + str(timp_stop_py - timp_start_py) + " cu algoritmul nativ din Python")
    print("\n - a durat " + str(timp_stop_py - timp_start_py) + " cu algoritmul nativ din Python", end = '')

    cnt_ch = 0
    for sort in sorts:
        timp_start = time.time()
        myList = sort(lista, test[0], test[1] - 1)
        timp_stop = time.time()

        if lista_py == myList:
            status = " OK"
        else: 
            status = " Failed =(("

        g.write("\n - a durat " + str(timp_stop - timp_start) + status + " cu metoda " + ch_sorts[cnt_ch])
        print("\n - a durat " + str(timp_stop - timp_start) + status + " cu metoda " + ch_sorts[cnt_ch], end = '')
        cnt_ch += 1

g.close()