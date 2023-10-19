import pandas as pd
import pygame
import matplotlib.pyplot as plt
import time
from beehive import * 
pygame.init()

#Affiche la route de l'abeille avec pygame
def display_route(bee):
    #Paramètres
    XB , YB = bee.HQ
    BCOLOR = (255,255,0)
    HIVECOLOR = (0,0,255)
    WIDTH = 825 #
    RATIO = WIDTH/1000 #Peut être modifié. Permet à mon petit écran de tout afficher
    SCREEN = pygame.display.set_mode((WIDTH,WIDTH))
    
    pygame.draw.circle(SCREEN, HIVECOLOR , (XB*RATIO,YB*RATIO) , 5)
    for flower in FIELD:
        x,y = flower
        pygame.draw.circle(SCREEN, BCOLOR , (x*RATIO,y*RATIO) , 4)
    pygame.display.flip()
    
    route = bee.route
    pygame.draw.line(SCREEN, HIVECOLOR, (XB*RATIO,YB*RATIO), (route[0][0]*RATIO,route[0][1]*RATIO))
    for i,flower in enumerate(route):
        if i==0: continue
        pygame.draw.line(SCREEN, BCOLOR, ((route[i-1][0]*RATIO,route[i-1][1]*RATIO)) , (flower[0]*RATIO,flower[1]*RATIO))
        pygame.display.flip()
        time.sleep(0.05)
    pygame.draw.line(SCREEN, HIVECOLOR, ((route[-1][0]*RATIO,route[-1][1]*RATIO)) , (XB*RATIO,YB*RATIO) )
    pygame.display.flip()
    pygame.image.save(SCREEN, f"files/{round(topscore,3)}score_route.png")

#Récupération des coordonnées des fleurs, dans le fichier excel   
df = pd.read_excel('field.xlsx')
FIELD = []
for x,y in zip(df['x'] , df['y']):
    FIELD.append((x,y))


#Création des 100 abeilles à route aléatoire, et de la ruche
roster = []
for i in range(100):
    field_copy = FIELD[:]
    rd.shuffle(field_copy)
    roster.append(Bee(field_copy))
hive = Hive(roster)


topscores = [] #Enregistre le score de la meilleur abeille à chaque génération

#GENS = 30000
GENS = int(input('Entrez le nombre de générations à simuler : '))
start = time.time()
for i in range(GENS):
    topscores.append(hive.get_best_score()) 
    hive.evolve() #Evolution
end = time.time()
print(f"Temps d'éxécution : {end-start} s")
topscore = topscores[-1] #Le score optimal final
print(f"Score optimal : {topscore}")

#Représentation graphique du meilleur score en fonction du nombre de générations
plt.plot(topscores)
plt.xlabel("Nombre de générations")
plt.ylabel("Meilleur score")
plt.savefig(f"files/{GENS}gens_{round(topscore,3)}score_fig.png")
plt.show()

display_route(hive.get_best_bee()) #Affichage de la route de l'abeille la plus performante

#Prompt pour l'utilisateur
print(f"Graphique sauvegardé dans le dossier files sous le nom : {GENS}gens_{round(topscore,3)}score_fig.png")
print(f"Affichage de la route sauvegardée dans le dossier files sous le nom : {round(topscore,3)}score_route.png")


