import sys
import timeit
nb_iti = 0

def convertStringToNumber(array):
    liste = []
    for i in range(len(array)):
        liste.append(float(array[i]))
    return liste

def quick_sort(arr, lo=0, hi=None):

    if hi is None:
        hi = len(arr) - 1

    if lo < hi:
        p = partition(arr, lo, hi)

        quick_sort(arr, lo, p - 1)
        quick_sort(arr, p + 1, hi)

    return arr

def partition(arr, lo, hi):

    pivot_index = hi
    l = lo

    for i in range(lo, hi):
        if arr[i] <= arr[pivot_index]:
            swap(arr, i, l)
            l = l + 1

    swap(arr, l, pivot_index)

    return l

def swap(arr, left, right):
    arr[left], arr[right] = arr[right], arr[left]

tab = convertStringToNumber(sys.argv[1].split(";"))

quick_sort(tab)

print("Serie")
print(convertStringToNumber(sys.argv[1].split(";")))
print("Resultat")
print(tab)
print("Nb de comparaison")
print(nb_iti)
print("Nb d iteration")
print(nb_iti)
print("Temps (sec)")
execution_time = timeit.timeit('quick_sort(tab)', 'from __main__ import quick_sort, tab', number=1)
print(execution_time)