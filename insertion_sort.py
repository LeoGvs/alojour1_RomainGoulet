
def tri_insertion(tab): 
    print(tab)
    
    for i in range(1, len(tab)): 
        k = float(tab[i]) 
        print(k)
        j = i-1
        print(j)
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k


tab = [200, 12, -18, 30, 2, 74, 6.3, 70]
tri_insertion(tab) 
print ("Le tableau trié est:")
for i in range(len(tab)): 
    print ("% d" % float(tab[i]))
