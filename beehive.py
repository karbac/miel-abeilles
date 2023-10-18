import random as rd


class Bee:
    def __init__(self, route):
        self.route = route  #
        self.HQ = (500,500) #Localisation de la ruche
        self.N = len(route)

    #Distance de Manhattan entre deux points
    def d(self, ta,tb):
        return abs(tb[0]-ta[0]) + abs(tb[1]-ta[1])

    #Distance moyenne de Manhattan par étape
    def get_score(self):
        return (sum([self.d(self.route[i+1] , self.route[i]) for i in range(self.N-1)]) +  self.d(self.HQ, self.route[0]) + self.d(self.route[-1] , self.HQ)) / (self.N + 1)       




class Hive:
    def __init__(self, roster):
        self.roster = roster #Tableau de 100 abeilles
        self.N = len(roster)
        
    #Distance de Manhattan entre deux points
    def d(self, ta,tb):
        return abs(tb[0]-ta[0]) + abs(tb[1]-ta[1])

    #Retourne le score de l'abeille la plus performante de la ruche
    def get_best_score(self):
        return self.get_best_bee().get_score()
    #Retourne l'abeille la plus performante de la ruche
    def get_best_bee(self):
        return sorted(self.roster, key= lambda x : x.get_score())[0]


    #Retourne un tableau des 50 abeilles sélectionnées
    def select(self):
        return sorted(self.roster, key= lambda x : x.get_score())[:50] #50 meilleurs scores
    def roulette_select(self):
        return rd.choices(sorted(self.roster, key= lambda x : x.get_score(),reverse=True) , cum_weights = [1]*self.N , k = 50)
    #Croisement de 2 abeilles
    #Retourne un tuple de deux abeilles enfants
    def crossover(self, bee_1, bee_2):
        route_1 = bee_1.route[:]
        route_2 = bee_2.route[:]
        p1,p2 = rd.sample( range(bee_1.N), 2)
        p1,p2 = min(p1,p2) , max(p1,p2)
        child_route_1 = []
        child_route_2 = []
        [child_route_1.append(x) for x in route_1[p1:p2] + route_2 if x not in child_route_1]
        [child_route_2.append(x) for x in route_2[p1:p2] + route_1 if x not in child_route_2]
        return ( Bee(child_route_1) , Bee(child_route_2) )

    
        
    #Effectue une mutation d'une abeille
    def mutate(self, bee):
        i,j = rd.sample( range(len(bee.route)) , 2)
        i,j = min(i,j), max(i,j)
        if rd.random() > 0.5:
            bee.route[i] , bee.route[j] = bee.route[j] , bee.route[i] #Permutation de deux fleurs dans la route
        else:
            bee.route = bee.route[:i] + bee.route[i:j+1][::-1] + bee.route[j+1:] #Inversion d'une portion de route
        
                    
    #Evolution de la ruche
    def evolve(self):
        toprunners = self.select() #SELECTION
        children = []
        for i in range(0,50,2): 
            child_1 , child_2 = self.crossover(toprunners[i] , toprunners[i+1]) #CROISEMENT - Génération des enfants
            #MUTATION
            self.mutate(child_1)
            self.mutate(child_2)
            children += [child_1, child_2]
        self.roster = sorted(self.roster + children, key = lambda x: x.get_score())[:100] #EVALUATION - On garde les 100 abeilles les plus performantes
            
        
        
           
        
        
        
        
    
                
        
