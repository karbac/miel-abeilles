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

    
    #Retourne un tableau des 50 abeilles sélectionnées
    def select(self):
        return sorted(self.roster, key= lambda x : x.get_score())[:50] #50 meilleurs scores

    def get_best_score(self):
        return sorted(self.roster, key= lambda x : x.get_score())[0].get_score()

    def get_best_bee(self):
        return sorted(self.roster, key= lambda x : x.get_score())[0]
    
    def get_average_score(self):
        return sum([x.get_score() for x in self.roster])/len(self.roster)
    
    #Croisement de 2 abeilles
    #Retourne un tuple de deux abeilles enfants
    def cross(self, bee_1, bee_2):
        gnm_1 = bee_1.genome[:]
        gnm_2 = bee_2.genome[:]
        child_gnm_1 = gnm_1[:25]
        child_gnm_2 = gnm_2[25:]
        for i in range(50):
            if gnm_2[i] not in child_gnm_1:
                child_gnm_1.append(gnm_2[i])
            if gnm_1[i] not in child_gnm_2:
                child_gnm_2.append(gnm_1[i])           

        return ( Bee(child_gnm_1) , Bee(child_gnm_2) )

        
        
    def mutate(self, bee):
        #average = child.get_score() / 51
        gnm = bee.genome[:]
        bhv = bee.beehive
        for i in range(1,50):
            if i==1:
                if self.d(bhv,gnm[i]) + self.d(gnm[i+1] , gnm[i-1]) < self.d(bhv,gnm[i-1]) + self.d(gnm[i+1] , gnm[i]):
                    bee.genome[i] , bee.genome[i-1] = bee.genome[i-1] , bee.genome[i]
                continue
            if i==49:
                if self.d(gnm[i-2] , gnm[i]) + self.d(bhv, gnm[i-1]) < self.d(gnm[i-2] , gnm[i-1]) + self.d(bhv,gnm[i]):
                    bee.genome[i] , bee.genome[i-1] = bee.genome[i-1] , bee.genome[i]
                continue
            if self.d(gnm[i-2] , gnm[i]) + self.d(gnm[i+1],gnm[i-1]) < self.d(gnm[i-2] , gnm[i-1]) + self.d(gnm[i] , gnm[i+1]):
                bee.genome[i] , bee.genome[i-1] = bee.genome[i-1] , bee.genome[i]
    
    def mutate(self,bee):
        i_max = 0
        d_max = 0
        gnm = bee.genome[:]
        for i,flower in enumerate(gnm):
            if i==0: continue
            if i==49: continue
            if self.d(flower,gnm[i-1]) > d_max:
                i_max = i
                d_max = self.d(flower,gnm[i-1])
                
        diff_max = 0
        j_max = 0
        for j in range(1,49):
            if j in (i_max , i_max-1): continue
            new_dist = self.d(gnm[j-1],gnm[i_max]) + self.d(gnm[i_max],gnm[j+1]) + self.d(gnm[i_max-1],gnm[j]) + self.d(gnm[j],gnm[i_max+1])
            old_dist = self.d(gnm[j-1],gnm[j]) + self.d(gnm[j],gnm[j+1]) + self.d(gnm[i_max-1],gnm[i_max]) + self.d(gnm[i_max],gnm[i_max+1])
            diff = old_dist - new_dist
            if diff > diff_max:
                diff_max = diff
                j_max = j
        bee.genome[i_max] , bee.genome[j_max] = bee.genome[j_max] , bee.genome[i_max]      
                                                        
        
            
        
                    
    
    def evolve(self,mutation=False):
        toprunners = self.select()
        children = []
        for i in range(0,50,2):
            child_1 , child_2 = self.cross(toprunners[i] , toprunners[i+1])
            children += [child_1, child_2]
        if mutation:
            for child in children:
                self.mutate(child)
        self.roster = toprunners + children
        
            
        
        
           
        
        
        
        
    
                
        
