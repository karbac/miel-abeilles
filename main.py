import pandas as pd
import pygame
import matplotlib.pyplot as plt
import time
from beehive import * 
pygame.init()

def show_course(bee):
    genome = bee.genome
    pygame.draw.line(SCREEN, HIVECOLOR, (XB*RATIO,YB*RATIO), (genome[0][0]*RATIO,genome[0][1]*RATIO))
    for i,flower in enumerate(genome):
        if i==0: continue
        pygame.draw.line(SCREEN, BCOLOR, ((genome[i-1][0]*RATIO,genome[i-1][1]*RATIO)) , (flower[0]*RATIO,flower[1]*RATIO))
        #pygame.display.flip()
        #time.sleep(0.25)
    
    pygame.draw.line(SCREEN, HIVECOLOR, ((genome[-1][0]*RATIO,genome[-1][1]*RATIO)) , (XB*RATIO,YB*RATIO) )
    pygame.display.flip()

def show_field():
    pygame.draw.circle(SCREEN, HIVECOLOR , (XB*RATIO,YB*RATIO) , 5)
    for flower in FIELD:
        x,y = flower
        pygame.draw.circle(SCREEN, BCOLOR , (x*RATIO,y*RATIO) , 2)
    pygame.display.flip()
    
df = pd.read_excel('field.xlsx')
FIELD = []
for x,y in zip(df['x'] , df['y']):
    FIELD.append((x,y))


BEEHIVE = (500,500)
XB , YB = BEEHIVE
BCOLOR = (255,255,0)
HIVECOLOR = (0,0,255)
WIDTH = 825
RATIO = WIDTH/1000
#SCREEN = pygame.display.set_mode((WIDTH,WIDTH))
PHASE = 25

#Initialisation
roster = []
for i in range(100):
    field_copy = FIELD[:]
    rd.shuffle(field_copy)
    roster.append(Bee(field_copy))
hive = Hive(roster)



scores = []
for i in range(500):
    scores.append(hive.get_best_score())
    if i >= PHASE and scores[i] == scores[i-PHASE]:
        hive.evolve(mutation=True)
        print(f"mutate @ {i}")
    else: hive.evolve()
        
print(scores[-1])
plt.plot(scores)
plt.show()


