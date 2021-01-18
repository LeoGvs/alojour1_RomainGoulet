# Rendu algo jour 1
# Groupe Léo Gourvès, Romain Goulet, Nathan Rotsztein / Discord : TD 5

Bonjour, nous avons ici expliqué le fonctionnement des différents algorithmes avec nos mots, suite à cela nous avons rédigé notre constat sur le tri le plus intéressant.


# Le tri bulle : 

Cet algorithme de tri permet de trier les éléments d'un tableau d'une certaine manière, voici son fonctionnement:  

L'algorithme va comparer les valeurs deux par deux : il comparera la première valeur avec la deuxième puis la deuxième avec la troisième puis la troisième avec la quatrième etc, en plaçant toujours la valeur la plus petite (des deux valeurs comparées) la plus à gauche des valeurs comparées.

Ensuite l'algorithme va refaire exactement le même procédé mais avec le nouvel ordre obtenu, il comparera donc première valeur avec la deuxième puis la deuxième avec la troisième puis la troisième avec la quatrième etc.

Avec se procéder l'algorithme place donc à droite les valeurs les plus grandes. Il place d'abord la plus grande valeur toute à droite puis l'avant-dernière etc, jusqu'à avoir fini de classer tous le tableau

Notons que lorsque l'algorithme à placer les plus grandes valeurs à droite il ne les compare plus et réitère sont précédés en les ignorant.

Ainsi nous aurons à la fin un tableau dont les valeurs sont classé de la plus petite à la plus grande.



# Le tri de séléction : 

Ici l'algorithme va prendre la première valeur du tableau comme valeur témoin et la placer à part. Il va la comparer avec la deuxième puis la troisième puis la quatrième etc. jusqu'à trouver une valeur plus petite que la sienne. Une fois trouvé, la valeur témoin ( ici la première ) prendra la place (dans l'ordre des valeurs du tableau) de la nouvelle plus petite valeur trouvée.

Par la suite la nouvelle plus petite valeur deviendra la valeur témoin et va à son tour être comparée. Notons qu'elle sera comparée avec les valeurs à droite dans son ancienne position dans le tableau. 
Si elle est comparée à une valeur plus petite, elle prendra la place de cette valeur et la nouvelle valeur plus petite deviendra à son tour la valeur témoins, sinon elle se placera en premiere position du tableau et la deuxieme valeur du tableau deviendra la valeur témoin et l'algorythme continura son déroulement.   

L'algorithme réitère cette opération, ainsi nous aurons à la fin un tableau dont les valeurs sont classé de la plus petite à la plus grande.



# Le tri d'insertion : 

Ici l'algorithme va prendre la deuxième valeur du tableau et la comparer avec la première, il placera ensuite la plus petite valeur des deux en première dans le tableau.

L'algorithme va ensuite prendre la troisième valeur du tableau pour la comparer avec la deuxième.

-   Si la troisième valeur est plus petite que la deuxième : l'algorithme va comparer la troisième valeur à la première. 
        -   Ici si la troisième valeur est également plus petite que la première elle sera placé en première dans le tableau et décalera les valeurs du tableau d'un cran (l'ancienne première passera en deuxième valeur du tableau etc.) 
        -   Sinon la troisième valeur se placera en deuxième dans le tableau et décalera également le tableau d'un cran (l'ancienne deuxième passera en troisième valeur du tableau etc.).

-   Si la troisième valeur est plus grande que la deuxième alors (rien ne se passe) l'ordre des valeurs n'est pas changé.

L'algorithme va ensuite prendre la quatrième valeur pour la comparer avec la troisième si la quatrième est inférieure à la troisième il la comparera avec la deuxième et si elle aussi est inférieur à la quatrième il la comparera avec la première afin de la placer aux bons endroits dans le tableau.

L'algorithme réitère cette opération avec les valeurs toutes du tableau

Ainsi nous aurons à la fin un tableau dont les valeurs sont classé de la plus petite à la plus grande.



# Le tri fusion : 

Ici l'algorythme devise en deux moitiés les valeurs du tableau. Chacunes des parties vont être triés si elle ne les sont pas déjà, puis nous allons assembler les partie trié ensemble pour obtenir un tableau de valeurs triés. 



# Le tri rapide : 

Cet algorithme va partionné le tableau en plusieurs parties qui vont chacunes être partionné en deux sous listes (celle de gauche et celle de droite). Notons que la césure n'est pas forcément au milieu de la partie. Nous aurons donc un désiquilibre entre les tailles des sous partie.

Sous partie vont être par la suite trié






# Le tri à peigne :

Le tri à peigne est une amélioration du tri à bulles Son objectif est de réduire le temps de tri des valeurs les plus basses, qui pénalisait les performances de celui ci .
Pour cela, 2 valeurs sont comparées entres elles, espacées d'un certain interval, celui ci se réduisant progressivement, leur position est échangée selon si l'une des valeur est plus grande ou plus petite que l'autre

Le facteur de réduction optimal de cet interval serait de 1.3 (suite à des essais empiriques)

Complexité en temps Pire cas : O(n^2) Meilleur cas : O(n log n)

Complexité en espace Pire cas : O(1)




# Conclusion :

Suite à nos résultats nous avons pu en conclure que le tri le plus intéressant est le tri fusion, en effet c'est celui qui arrive à trier l'ensemble du tableau avec le moins de comparaisons effectuées, c'est également un de ceux qui a mis le moins de temps.
