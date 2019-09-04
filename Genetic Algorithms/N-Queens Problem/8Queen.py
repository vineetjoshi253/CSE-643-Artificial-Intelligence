import random
import copy
import matplotlib.pyplot as plt
import numpy as np


POPULATION_SIZE = 100
TOPK= 10
QUEENS = 8
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
    #Test For Column Collision
    for i in range(0, len(Chromo)):
        for j in range(0, len(Chromo)):
            if i != j:
                if Chromo[i] == Chromo[j]:
                    fitness += 1

    #Test for Diagonal Collision
    for k in range(0, len(Chromo)):
        for i in range(0, len(Chromo)):
            for j in range(0, len(Chromo)):
                if i - k == j - Chromo[k] and Chromo[i] == j and Chromo[i] != Chromo[k]:
                    fitness += 1

                elif i + j == Chromo[k] + k and Chromo[i] == j and Chromo[i] != Chromo[k]:
                    fitness += 1

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
    Child1 = []
    Child2 = []

    for i in range(QUEENS):
        if(Chromo1[i] == Chromo2[i]):
            Child1.append(Chromo1[i])
            Child2.append(Chromo2[i])
        else:
            Child1.append(random.randint(1,QUEENS))
            Child2.append(random.randint(1,QUEENS))
        
    return Child1,Child2
    
def Mutate(Children):
    for i in range(len(Children)):
        Children[i][random.randint(0,QUEENS-1)]=random.randint(1,QUEENS)
    return Children
        
def newGen(PoP):
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
        
           Child1,Child2=Crossover(PoP[i],PoP[j])
           Children.append(Child1)
           Children.append(Child2)
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
    MAX = []
    MIN = []
    PoP = InitialPopulation(PoP)
    PoPFitness = EvaluatePopulation(PoP)
    print("Generation: ",gen,sep="")
    print("Best Fitness Value: ",min(PoPFitness)," ","Worst Fitness Value: ",max(PoPFitness),sep="")
    MAX.append(max(PoPFitness))
    MIN.append(min(PoPFitness))
    ind = GoalTest(PoPFitness)
    while(ind==-1):
        PoP,PoPFitness = FindFittest(PoP,PoPFitness)
        gen+=1
        PoP = newGen(PoP)  
        PoPFitness = EvaluatePopulation(PoP)
        print("Generation: ",gen,sep="")
        print("Best Fitness Value: ",min(PoPFitness)," ","Worst Fitness Value: ",max(PoPFitness),sep="")
        MAX.append(max(PoPFitness))
        MIN.append(min(PoPFitness))
        ind = GoalTest(PoPFitness)
    
    print("SOLUTION FOUND!:")
    for i in range(QUEENS):
        for j in range(QUEENS):
            if j == PoP[ind][i]-1:
                print(" Q ",end="")
            else:
                print(" - ",end="")
        print()
    
    
    print("CONVERGENCE: ")
    barWidth = 0.5
    
    plt.rcParams['figure.figsize']=(10,6)
    Space1 = np.arange(len(MAX))
    Space2 = [x + barWidth for x in Space1]
    
    plt.bar(Space1, MAX, color='#7f6d5f', width=barWidth, edgecolor='white', label='MAX')
    plt.bar(Space2, MIN, color='#557f2d', width=barWidth, edgecolor='white', label='MIN')
            
    plt.xlabel('GENERATIONS', fontweight='bold')
    
    plt.legend()
    plt.show()



    
    
    