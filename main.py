import pandas as pd
import pygame
import matplotlib.pyplot as plt
import time
from beehive import * 
pygame.init()

def display_route(bee):
    HQ = (500,500)
    XB , YB = HQ
    BCOLOR = (255,255,0)
    HIVECOLOR = (0,0,255)
    WIDTH = 825
    RATIO = WIDTH/1000
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
        time.sleep(0.1)
    
    pygame.draw.line(SCREEN, HIVECOLOR, ((route[-1][0]*RATIO,route[-1][1]*RATIO)) , (XB*RATIO,YB*RATIO) )
    pygame.display.flip()
    pygame.image.save(SCREEN, f"files/{round(topscore,3)}score_route.png")

    
df = pd.read_excel('field.xlsx')
FIELD = []
for x,y in zip(df['x'] , df['y']):
    FIELD.append((x,y))



#Initialisation
roster = []
for i in range(100):
    field_copy = FIELD[:]
    rd.shuffle(field_copy)
    roster.append(Bee(field_copy))
hive = Hive(roster)


topscores = []

start = time.time()
GENS = 50000
for i in range(GENS):
    topscores.append(hive.get_best_score())
    hive.evolve()
end = time.time()
print(end-start)
topscore = topscores[-1]
print(topscore)

plt.plot(topscores)
plt.xlabel("Nombre de générations")
plt.ylabel("Meilleur score")
plt.savefig(f"files/{GENS}gens_{round(topscore,3)}score_fig.png")
plt.show()

display_route(hive.get_best_bee())


