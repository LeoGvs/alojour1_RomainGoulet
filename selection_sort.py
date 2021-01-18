import sys
import timeit
nb_iti = 0

def convertStringToNumber(array):
    liste = []
    for i in range(len(array)):
        liste.append(float(array[i]))
    return liste

def selection_sort(tab):

   for i in range(len(tab)):
       min = i

       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j
                
       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp

   return tab

tab = convertStringToNumber(sys.argv[1].split(";"))
sorted_tab = []

selection_sort(tab)
 
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
execution_time = timeit.timeit('selection_sort(tab)', 'from __main__ import selection_sort, tab', number=1)
print(execution_time)