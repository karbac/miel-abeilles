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

    def get_brut_score(self):
        score = 0
        for i,flower in enumerate(self.genome):
            if i==0: continue
            score += self.d(self.genome[i-1] , flower)
        return score
        

    def max_dist(self):
        dist = self.d(self.beehive, self.genome[0])
        for i,flower in enumerate(self.genome):
            if i==0: continue
            if self.d(self.genome[i-1], flower) > dist:
                dist = self.d(self.genome[i-1], flower)
        return dist
        




class Hive:
    def __init__(self, roster):
        self.roster = roster #Tableau de 100 abeilles
        
    #Distance de Manhattan entre deux points
    def d(self, ta,tb):
        return abs(tb[0]-ta[0]) + abs(tb[1]-ta[1])


    def get_best_score(self):
        return sorted(self.roster, key= lambda x : x.get_score())[0].get_score()

    def get_best_bee(self):
        return sorted(self.roster, key= lambda x : x.get_score())[0]
    def get_worst_bee(self):
        return sorted(self.roster, key= lambda x : x.get_score())[-1]
    
    def get_average_score(self):
        return sum([x.get_score() for x in self.roster])/len(self.roster)


    #Retourne un tableau des 50 abeilles sélectionnées
    def select(self):
        return sorted(self.roster, key= lambda x : x.get_score())[:50] #50 meilleurs scores
    #Croisement de 2 abeilles
    #Retourne un tuple de deux abeilles enfants
    def cross(self, bee_1, bee_2):
        gnm_1 = bee_1.genome[:]
        gnm_2 = bee_2.genome[:]
        p1 , p2 = rd.sample( range(len(gnm_1)) , 2)
        q1 , q2 = rd.sample( range(len(gnm_2)) , 2)
        if p2 > p1:
            p1, p2 = p2, p1
        if q1 > q2:
            q1, q2 = q2, q1
        child_gnm_1 = []
        child_gnm_2 = []
        [child_gnm_1.append(x) for x in gnm_1[p1:p2+1] + gnm_2 if x not in child_gnm_1]
        [child_gnm_2.append(x) for x in gnm_2[q1:q2+1] + gnm_1 if x not in child_gnm_2]
        return ( Bee(child_gnm_1) , Bee(child_gnm_2) )

    
        
        
    def mutate2(self, bee):
        gnm = bee.genome[:] + [bee.beehive]
        for i in range(49):
            for j in range(i,50):                
                old_score = self.d(gnm[i-1],gnm[i]) + self.d(gnm[i],gnm[i+1]) + self.d(gnm[j-1],gnm[j]) + self.d(gnm[j],gnm[j+1])
                new_score = self.d(gnm[i-1],gnm[j]) + self.d(gnm[j],gnm[i+1]) + self.d(gnm[j-1],gnm[i]) + self.d(gnm[i],gnm[j+1]) 
                diff = old_score - new_score
                if diff > 0:
                    bee.genome[i] , bee.genome[j] = bee.genome[j] , bee.genome[i]        
        
            
    def mutate(self, bee):
        i,j = rd.sample( range(len(bee.genome)) , 2)
        bee.genome[i] , bee.genome[j] = bee.genome[j] , bee.genome[i]
        
                    
    
    def evolve(self,mutation=False):
        toprunners = self.select() #SELECTION
        children = []
        for i in range(0,50,2): #EVOLUTION
            child_1 , child_2 = self.cross(toprunners[i] , toprunners[i+1])
            children += [child_1, child_2]
            if mutation: #MUTATION
                self.mutate(child_1)
                self.mutate(child_2)
        self.roster = sorted(self.roster + children, key= lambda x: x.get_score())[:100] #EVALUATION
            
        
        
           
        
        
        
        
    
                
        
