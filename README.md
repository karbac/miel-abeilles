# CONTEXTE DU PROBLEME
Nous mettons en scène des abeilles qui doivent aller butiner des fleurs.  
Les abeilles démarrent de la ruche, visitent les fleurs une à une, puis retournent à la ruche.    
Les 50 fleurs à butiner sont représentées par un tuple de coordonnées (x,y), qui nous est fourni - voir ***field.xlsx***  
Une abeille est définie par l'ordre dans lequel elle ira butiner les fleurs. On représentera cela par une liste de 50 fleurs que l'on appelera **route**.  
L'objectif est de trouver une route qui optimise le temps de parcours des abeilles.   
On se propose de résoudre ce problème avec un **algorithme génétique**.   

# ALGORITHME GENETIQUE
Nous démarrons avec une ruche de 100 abeilles, ayant chacune une route aléatoire.  
Le **score** d'une abeille est défini par la distance moyenne qu'elle parcourt d'une fleur à une autre.  
Ainsi, le score dépend de la **route** et définit sa **performance** : Une abeille est d'autant plus performante que son score est bas.  
La distance employée est la **distance de Manhattan**, dans un souci d'optimisation de complexité.  
L'objectif est donc de **minimiser le score**.    
Notre ruche de départ représente la **génération 0**, et passer d'une génération à la suivante s'effectue par un processus d'**évolution**.  
Nous allons ainsi soumettre notre ruche à plusieurs évolutions successives, dans le but d'optimiser notre route.  
Une **évolution** se décompose en plusieurs étapes :  La **sélection**, Le **croisement**, La **mutation** et l'**évaluation**.  

## SELECTION
Nous sélectionnons 50 abeilles parmi les 100 pour effectuer un croisement.    
Les 50 abeilles que nous sélectionnons sont simplement les 50 abeilles les plus performantes.

## CROISEMENT
Les abeilles sélectionnées subissent un croisement. Elles sont regroupées par couple, et chaque couple génère 2 abeilles enfants.    
Nous générons la route des abeilles enfants en copiant une sous-partie au hasard de la route d'un parent et en complétant par les fleurs de la route de l'autre parent, par ordre d'apparition.  
Nous avons ainsi généré 50 enfants.

## MUTATION
Les enfants générés subissent une mutation, c'est-à-dire un changement dans leur route. Cette opération a pour but de générer plus de diversité.   
Nous effectuons, au pile ou face, soit une inversion d'une sous-partie aléatoire de la route, soit une permutation de deux fleurs aléatoires dans la route.

## EVALUATION
Avec les 100 abeilles originelles et les 50 enfants générés, nous avons un total de 150 abeilles.  
Pour conserver un total de 100 abeilles dans la ruche, le score de chaque abeille est évalué, et les 50 abeilles les moins performantes sont évincées.

## REMARQUES
Les critères de sélection, croisement et mutation choisis ici sont totalement arbitraires, et une multitude d'autres solutions sont possibles.  
L'objectif est de générer assez de diversité afin qu'au bout d'un grand nombre de générations, nous puissions obtenir une solution optimale.  
Le processus d'évaluation n'est pas modifiable. Il est impératif de conserver les abeilles les plus performantes afin d'évoluer dans la poursuite de notre objectif.

# ARCHITECTURE
## *beehive.py*
Contient la logique des classes ***Bee*** et ***Hive***.  
La classe ***Bee*** représente une abeille. La classe ***Hive*** représente la ruche
## *Main.py*
Le programme principal. Prend en entrée un nombre de générations à simuler.  
Génère le graphique de l'évolution du score de la meilleure abeille de chaque génération, en fonction du nombre de générations.    
Génère également l'affichage de la route de l'abeille la plus performante de la dernière génération.  
Sur le rendu graphique, la ruche est représentée en bleu, et les fleurs sont représentées par des points verts.
## Dossier *files*
Contient les graphiques et les affichages de routes générés, au format png.

# PERFORMANCE & NOTES
Cet algorithme est de complexité temporelle **O(N)** , **N** étant le nombre de générations à simuler.   
En effet, l'algorithme d'évolution s'éxécute à une vitesse qui ne dépend pas de N.  

Le score est décroissant en fonction du nombre de générations, et il décroît de plus en plus lentement jusqu'à finir par stagner.  
Empiriquement, on observe que le score idéal se situe entre **146** et **147**.    
Théoriquement, le score devrait décroître jusqu'à atteindre le score idéal, mais en pratique, l'atteinte du score idéal peut nécéssiter que l'algorithme tourne pendant des heures.  
Cependant, pour ce modèle, on obtient des résultats assez proches et satisfaisants, en simulant entre **25000** et **40000** générations, point où le score commence à stagner longuement.  
Le temps d'éxécution pour une simulation de 25000 générations est d'environ **4 minutes**, et pour 40000 générations, il est d'environ **6 à 7 minutes**.  
Il conviendrait d'essayer différents modèles afin de trouver une solution plus performante. Il suffit pour cela de modifier la fonction de sélection, de croisement et/ou de mutation.  
Ceci est en tous cas la meilleure solution que j'ai pu trouver.  

# TERMINOLOGIE DE CODE
## Classe ***Bee***
***route*** - Liste de 50 tuples représentant les coordonnées des fleurs à butiner. L'ordre de la liste définit l'ordre de parcours de l'abeille.  
***HQ*** - Quartier général des abeilles. Tuple représentant les coordonnées de la ruche, point de départ et d'arrivée des abeilles.  
***N*** - Nombre de fleurs dans la route.  
## Classe ***Hive***
***roster*** - Liste de 100 objets de type ***Bee***, abeilles composant la ruche.  
***N*** - Nombre d'abeilles dans la ruche.  


