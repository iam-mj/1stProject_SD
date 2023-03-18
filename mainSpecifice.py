import time
from generate import gen
from genTesteSpeciale import cresc, descresc, aproapeSortat, apropiat
from mergesort import merge
from bucketsort import bucket
from quicksort import quick
from radixsort import radix
from radixsort4 import radix4
from radixsort8 import radix8
from radixsort16 import radix16
from shellsort import shell
from countsort import count

i = "Specifice1"
g = open("rezultate" + i + ".txt", "w")
sorts = [radix, radix4, radix8, radix16, shell, merge, bucket, count]
ch_sorts = ["radix", "radix4", "radix8", "radix16", "shell", "merge", "bucket", "count"]
testeSpeciale = [cresc, descresc, aproapeSortat, apropiat]
ch_testeSpeciale = ["cresc", "descresc", "aproapeSortat", "apropiat"]

cnt = 0
for test in testeSpeciale:
    cnt += 1
    #generam numerele
    lista = test(10 ** 6, 10 ** 6)
    
    g.write("\n Testul " + ch_testeSpeciale[cnt - 1] + " N = 1000000" + " Max = 1000000" + ":")
    print("\n Testul " + ch_testeSpeciale[cnt - 1] + " N = 1000000" + " Max = 1000000", end = ':')


    timp_start_py = time.time()
    lista_py = sorted(lista)
    timp_stop_py = time.time()

    g.write("\n - a durat " + str(timp_stop_py - timp_start_py) + " cu algoritmul nativ din Python")
    print("\n - a durat " + str(timp_stop_py - timp_start_py) + " cu algoritmul nativ din Python", end = '')

    cnt_ch = 0
    for sort in sorts:
        timp_start = time.time()
        myList = sort(lista, 10 ** 6, 10 ** 6)
        timp_stop = time.time()

        if lista_py == myList:
            status = " OK"
        else: 
            status = " Failed =(("

        g.write("\n - a durat " + str(timp_stop - timp_start) + status + " cu metoda " + ch_sorts[cnt_ch])
        print("\n - a durat " + str(timp_stop - timp_start) + status + " cu metoda " + ch_sorts[cnt_ch], end = '')
        cnt_ch += 1

g.close()