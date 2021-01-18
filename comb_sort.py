  
import sys

def convertStringToNumber(array):
    liste = []
    for i in range(len(array)):
        liste.append(float(array[i]))
    return liste

def nextInterval(interval): 
    interval = (interval * 10)//13 #13 est le facteur de réduction optimal x10
    if interval < 1: 
        return 1
    return interval 
 
def combSort(liste): 
    n = len(liste) 
    interval = n 
    echange = True

    while interval !=1 or echange == 1: 
        interval = nextInterval(interval) 
        echange = False
        
        for i in range(0, n-interval): 
            if liste[i] > liste[i + interval]: 
                liste[i], liste[i + interval]=liste[i + interval], liste[i] 
                echange = True

liste = convertStringToNumber(sys.argv[1].split(";"))
combSort(liste) 


print ("Liste triée:") 
for i in range(len(liste)): 
	print (liste[i]),
