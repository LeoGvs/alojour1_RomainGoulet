def nextInterval(interval): 
    interval = (interval * 10)//13 #13 est le facteur de réduction optimal x10
    if interval < 1: 
        return 1
    return interval 
 
def combSort(liste): 
    n = len(liste) 
    interval = n 
    échange = True

    while interval !=1 or échange == 1: 
        interval = nextInterval(interval) 
        échange = False
        
        for i in range(0, n-interval): 
            if liste[i] > liste[i + interval]: 
                liste[i], liste[i + interval]=liste[i + interval], liste[i] 
                échange = True


liste = [ 5, 500, 5, 1, 44.5, -23.5, -84.5, +28.0, 0] 
combSort(liste) 

print ("Liste triée:") 
for i in range(len(liste)): 
print (liste[i]), 
