
import sys
import timeit
nb_iti = 0

def convertStringToNumber(array):
    liste = []
    for i in range(len(array)):
        liste.append(float(array[i]))
    return liste

def insertion_sort(tab): 
    print(tab)
    
    for i in range(1, len(tab)): 
        k = float(tab[i]) 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k


tab = convertStringToNumber(sys.argv[1].split(";"))
sorted_tab = []

insertion_sort(tab)

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
execution_time = timeit.timeit('insertion_sort(tab)', 'from __main__ import insertion_sort, tab', number=1)
print(execution_time)
