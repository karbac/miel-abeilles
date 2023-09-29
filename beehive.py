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
    def cross2(self, bee_1, bee_2):
        gnm_1 = bee_1.genome[:]
        gnm_2 = bee_2.genome[:]
        child_gnm_1
        child_gnm_2

        return ( Bee(child_gnm_1) , Bee(child_gnm_2) )

    def cross(self, bee_1, bee_2):
        RATIO = 1.1
        average = (( bee_1.get_score()+bee_2.get_score() )/102) * 0.5
        
        gnm_1 , gnm_2  = bee_1.genome[:] , bee_2.genome[:]
        child_gnm_1 = [gnm_1[0]]
        child_gnm_2 = [gnm_2[0]]
        point = 0
        course = 0
        while len(child_gnm_1)<50 or len(child_gnm_2)<50:
            point = (point+1)%50
            course += 1
            f_1 = gnm_1[point]
            f_2 = gnm_2[point]
            g_1 = gnm_1[49-point]
            g_2 = gnm_2[49-point]
            if course > 49:
                average *= RATIO
                course = 0
                continue                   
                
            if f_2 not in child_gnm_1:
                if self.d(child_gnm_1[-1],f_2) < average:
                    child_gnm_1.append(f_2)
                    course = 0
            if f_1 not in child_gnm_1:
                if self.d(child_gnm_1[-1],f_1) < average:
                    child_gnm_1.append(f_1)
                    course = 0
            if g_1 not in child_gnm_2:
                if self.d(child_gnm_2[-1],g_1) < average:
                    child_gnm_2.append(g_1)
                    course = 0
            if g_2 not in child_gnm_2:
                if self.d(child_gnm_2[-1],g_2) < average:
                    child_gnm_2.append(g_2)
                    course = 0
        return ( Bee(child_gnm_1) , Bee(child_gnm_2))
    
        
        
    def mutate(self, bee):
        diff_max = 0
        i_max = -1
        j_max = -1
        gnm = bee.genome[:] + [bee.beehive]
        for i in range(49):
            for j in range(i,50):                
                old_score = self.d(gnm[i-1],gnm[i]) + self.d(gnm[i],gnm[i+1]) + self.d(gnm[j-1],gnm[j]) + self.d(gnm[j],gnm[j+1])
                new_score = self.d(gnm[i-1],gnm[j]) + self.d(gnm[j],gnm[i+1]) + self.d(gnm[j-1],gnm[i]) + self.d(gnm[i],gnm[j+1]) 
                diff = old_score - new_score
                if diff > diff_max:
                    diff_max = diff
                    i_max = i
                    j_max = j
        if i_max == -1:
            print('No')
            return
        bee.genome[i_max] , bee.genome[j_max] = bee.genome[j_max] , bee.genome[i_max]       
        
            
            
        
                    
    
    def evolve(self,mutation=False):
        toprunners = self.select()
        children = []
        for i in range(0,50,2):
            child_1 , child_2 = self.cross(toprunners[i] , toprunners[i+1])
            children += [child_1, child_2]
            if mutation:
                self.mutate(child_1)
                self.mutate(child_2)
        self.roster = toprunners + children
        
            
        
        
           
        
        
        
        
    
                
        
