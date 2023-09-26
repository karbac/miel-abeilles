import random as rd

class Bee:
    def __init__(self, genome):
        self.genome = genome
        self.beehive = (500,500)

    #Distance de Manhattan entre deux points
    def d(self, ta,tb):
        return abs(tb[0]-ta[0]) + abs(tb[1]-ta[1])

    #Distance parcourue par l'abeille
    def get_score(self):
        score = self.d(self.beehive, self.genome[0])
        for i,flower in enumerate(self.genome):
            if i==0: continue
            score += self.d(self.genome[i-1] , flower)
        score += self.d(self.genome[-1] , self.beehive)
        return score


class Hive:
    def __init__(self, roster):
        self.roster = roster #Tableau de 100 abeilles
        
    #Distance de Manhattan entre deux points
    def d(self, ta,tb):
        return abs(tb[0]-ta[0]) + abs(tb[1]-ta[1])

    
    #Retourne un tableau des 50 abeilles sélectionnées
    def select(self):
        return sorted(self.roster, key= lambda x : x.get_score())[:50] #50 meilleurs scores

    def get_best_score(self):
        return sorted(self.roster, key= lambda x : x.get_score())[0].get_score()
    
    #Croisement de 2 abeilles
    #Retourne un tuple de deux abeilles enfants
    def cross(self, bee_1, bee_2):
        genome_1 = bee_1.genome[:25]
        for flower in bee_2.genome:
            if flower not in genome_1: genome_1.append(flower)
        
        genome_2 = bee_2.genome[25:]
        for flower in bee_1.genome:
            if flower not in genome_2: genome_2 = [flower] + genome_2

        return (Bee(genome_1) , Bee(genome_2))
        
    def mutate(self, children):
        for child in children:
            average = child.get_score() / 51
            for i,flower in enumerate(child.genome):
                if i==0 or i==49: continue
                dist = self.d(flower,child.genome[i-1])
                if self.d(child.genome[i-1],child.genome[i+1]) < dist : child.genome[i] , child.genome[i+1] = child.genome[i+1] , child.genome[i] 
                    
    
    def evolve(self,mutation=False):
        toprunners = self.select()
        children = []
        for i in range(0,50,2):
            child_1 , child_2 = self.cross(toprunners[i] , toprunners[i+1])
            children += [child_1, child_2]
        if mutation:
            self.mutate(children)
        self.roster = toprunners + children
        
            
        
        
           
        
        
        
        
    
                
        
