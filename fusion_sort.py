import sys
import timeit
nb_iti = 0

def convertStringToNumber(array):
    liste = []
    for i in range(len(array)):
        liste.append(float(array[i]))
    return liste

def fusion_sort(tab):

    if len(tab) == 1:
        return tab

    middle = len(tab) // 2
    a = fusion_sort(tab[:middle])
    b = fusion_sort(tab[middle:])
    return merge(tab, a, b)

def merge(arr, a, b):

    i = 0
    j = 0
    k = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1

    return arr


tab = convertStringToNumber(sys.argv[1].split(";"))

fusion_sort(tab)

print("Serie")
print(convertStringToNumber(sys.argv[1].split(";")))
print("Resultat")
print(tab)
print("Nb de comparaison")
print(nb_iti)
print("Nb d iteration")
print(nb_iti)
print("Temps (sec)")
execution_time = timeit.timeit('fusion_sort(tab)', 'from __main__ import fusion_sort, tab', number=1)
print(execution_time)