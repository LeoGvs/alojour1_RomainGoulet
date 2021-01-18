# Rendu algo jour 1
# Groupe Léo Gourvès, Romain Goulet, Nathan Rotsztein



# Le tri à peigne ou comb sort :

Complexité en temps
Pire cas : O(n^2)
Meilleur cas : O(n log n)

Complexité en espace
Pire cas : O(1)

Le tri à peigne est une amélioration du tri à bulles
Son objectif est de réduire le temps de tri des valeurs les plus basses, qui pénalisait les performances de celui ci
Pour cela, 2 valeurs sont comparées entres elles, espacées d'un certain interval, celui ci se réduisant progressivement, leur position est échangée selon si l'une des valeur est plus grande ou plus petite que l'autre

Le facteur de réduction optimal de cet interval serait de 1.3 (suite à des essais empiriques)
