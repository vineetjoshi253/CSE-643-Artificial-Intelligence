import random
import copy

POPULATION_SIZE = 100
TOPK= 10
QUEENS = int(input("Enter The Number Of Queens: "))
gen = 1

def InitialPopulation(PoP):
    for i in range(POPULATION_SIZE):
        temp = []
        for i in range(QUEENS):
            temp.append(random.randint(1,QUEENS))
        PoP.append(temp)
    return PoP

def IntersectQueen(Chromo):
    fitness = 0
    for i in range(0, len(Chromo)):
        for j in range(0, len(Chromo)):
            if i != j:
                if Chromo[i] == Chromo[j]:
                    fitness += 1

    for i in range(0,len(Chromo)):
        k=i+1;j = Chromo[i]-2
        while k<len(Chromo) and j>=0:
            if Chromo[k] == j+1:
                fitness+=1
            k+=1;j-=1
            
        k=i-1;j=Chromo[i]        
        while k>=0 and j<len(Chromo):
            if Chromo[k] == j+1:
                fitness+=1
            k-=1; j+=1
    
    for i in range(0,len(Chromo)):
        k=i-1;j = Chromo[i]-2
        while k>=0 and j>=0:
            if Chromo[k] == j+1:
                fitness+=1
            k-=1;j-=1
            
        k=i+1;j=Chromo[i]        
        while k<len(Chromo) and j<len(Chromo):
            if Chromo[k] == j+1:
                fitness+=1
            k+=1; j+=1
    
    return int(fitness/2)          
                

def EvaluatePopulation(PoP):
    PoPFitness = []
    for Chromo in PoP:
       PoPFitness.append(IntersectQueen(Chromo))
    return PoPFitness

def FindFittest(PoP,PoPFitness):
    PoPFitness, PoP = zip(*sorted(zip(PoPFitness, PoP)))
    PoP = PoP[:TOPK]
    return list(PoP),list(PoPFitness[:TOPK])

def Crossover(Chromo1,Chromo2):
    Child = []
    
    for i in range(QUEENS):
        if(Chromo1[i] == Chromo2[i]):
            Child.append(Chromo1[i])
        else:
            Child.append(random.randint(1,QUEENS))
            
    return Child
    
def Mutate(Children):
    for i in range(len(Children)):
        Children[i][random.randint(0,QUEENS-1)]=random.randint(1,QUEENS)
    return Children
        
def newGen(PoP):
    global gen
    Children=[]
    for i in range((len(PoP))):
        for j in range(i+1,len(PoP)):
           if(PoP[i] == PoP[j]):
               temp = []
               for k in range(QUEENS):
                   temp.append(random.randint(1,QUEENS))
               PoP[i] = copy.deepcopy(temp)
               
               temp = []
               for k in range(QUEENS):
                   temp.append(random.randint(1,QUEENS))
               PoP[j] = copy.deepcopy(temp)
        
           Child=Crossover(PoP[i],PoP[j])
           Children.append(Child)
    Children = Mutate(Children)
    for i in range(len(Children)):
        PoP.append(Children[i])
    return PoP

def GoalTest(PoPFitness):
    for i in range(len(PoPFitness)):
        if(PoPFitness[i]==0):
            return i
    return -1

if __name__ == "__main__":
    PoP = []
    PoP = InitialPopulation(PoP)
    PoPFitness = EvaluatePopulation(PoP)
    print("Generation: ",gen,sep="")
    print("Best Fitness Value: ",min(PoPFitness)," ","Worst Fitness Value: ",max(PoPFitness),sep="")
    ind = GoalTest(PoPFitness)
    while(ind==-1):
        PoP,PoPFitness = FindFittest(PoP,PoPFitness)
        print(PoP[0],"Fitness -> ",PoPFitness[0],sep="")
        gen+=1
        PoP = newGen(PoP)  
        PoPFitness = EvaluatePopulation(PoP)
        print("Generation: ",gen,sep="")
        print("Best Fitness Value: ",min(PoPFitness)," ","Worst Fitness Value: ",max(PoPFitness),sep="")
        ind = GoalTest(PoPFitness)
            
    print("SOLUTION FOUND!:")
    print(PoP[ind])
      