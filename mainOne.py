#testeaza cate un singur sort
import time
from generate import gen
from mergesort import merge
from bucketsort import bucket
from quicksort import quick
from radixsort import radix
from radixsort4 import radix4
from radixsort8 import radix8
from radixsort16 import radix16
from shellsort import shell

f = open("tests.txt")
nr_teste = int([x for x in f.readline().split()][2])
#teste - lista cu informatii despre testele noastre
teste = []
for i in range(nr_teste):
    test = [x for x in f.readline().split()]
    test = [int(test[i]) for i in [2, 5]]
    teste.append(test)

cnt = 0
for test in teste:
    cnt += 1
    #generam numerele
    lista = gen(test[0], test[1])
    print("\n Testul " + str(cnt) + " N = " + str(test[0]) + " Max = " + str(test[1]), end = ':')

    lista_py = sorted(lista)
        
    timp_start = time.time()
        #myList = bucket(lista, test[0], test[1] - 1)
        #myList = merge(lista, 0, test[0] - 1)
        #myList = shell(lista, test[0])
    myList = radix8(lista, test[0], test[1] - 1)
        #myList = radix(lista, test[0], test[1] - 1)
    timp_stop = time.time()

    if lista_py == myList:
        status = " OK"
    else: 
        status = " Failed =(("
        print("Avem: ", myList)
        print("Trebuia: ", lista_py)

    print("\n - a durat " + str(timp_stop - timp_start) + status)