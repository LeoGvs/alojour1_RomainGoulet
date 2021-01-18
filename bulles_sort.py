import sys
import timeit
nb_iti = 0

def convertStringToNumber(array):
    liste = []
    for i in range(len(array)):
        liste.append(float(array[i]))
    return liste

def bulle_sort(tab, nb_iti):
    n = len(tab)
    for i in range(n):

        for j in range(0, n-i-1):
            nb_iti = nb_iti + 1
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]
    
    for idx, item in enumerate(tab):
        print(item)
        if (idx+1) % 10 == 0:
            print('did ten')
        return idx


tab = convertStringToNumber(sys.argv[1].split(";"))

original_tab = tab
sorted_tab = []

bulle_sort(tab, nb_iti)
 

for i in range(len(tab)):
    sorted_tab.append(tab[i])

print("Serie")
print(convertStringToNumber(sys.argv[1].split(";")))
print("Resultat")
print(sorted_tab)
print("Nb de comparaison")
print(nb_iti)
print("Nb d iteration")
print(nb_iti)
print("Temps (sec)")
execution_time = timeit.timeit('bulle_sort(tab, nb_iti)', 'from __main__ import bulle_sort, tab, nb_iti', number=1)
print(execution_time)