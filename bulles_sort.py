import sys
print(sys.argv[1])
argv = sys.argv[1]
array_argv = argv.split(';')
print(array_argv)

import timeit
nb_iti = 0

def bulle_sort(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0, n-i-1):
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]


tab = array_argv
original_tab = tab
sorted_tab = []

bulle_sort(tab)
 
print("Test")
for i in range(len(tab)):
    sorted_tab.append(tab[i])

print("Serie")
print(argv.split(';'))
print("Resultat")
print(sorted_tab)
print("Nb de comparaison")
print(nb_iti)
print("Temps (sec)")
execution_time = timeit.timeit(bulle_sort, number=100)
print(execution_time)