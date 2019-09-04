import copy
PATH = []


def GoalTest(State,GoalState):
    if(State == GoalState):
        return True;
    return False;

def swap(State, pos1, pos2): 
    Child = copy.deepcopy(State)
    Child[pos1], Child[pos2] = Child[pos2], Child[pos1] 
    return Child

def search(State):
    for i in range(len(State)):
        if State[i] == -1:
            return i
        
    return -1

def generateChildren(currentState,fringeNodes,visibleNodes,exploredNodes):
    ind = search(currentState)
    for state in visibleNodes:
        fringeNodes.append(state)
    
    visibleNodes = []
    
    if(ind == 0):
        Child1 = swap(currentState,0,1)
        Child2 = swap(currentState,0,3)
        if Child1 not in exploredNodes:
            visibleNodes.append(Child1)
        if Child2 not in exploredNodes:
            visibleNodes.append(Child2)
    elif(ind == 2):
        Child1 = swap(currentState,1,2)
        Child2 = swap(currentState,2,5)
        if Child1 not in exploredNodes:
            visibleNodes.append(Child1)
        if Child2 not in exploredNodes:
            visibleNodes.append(Child2)
    elif(ind == 6):
        Child1 = swap(currentState,6,3)
        Child2 = swap(currentState,6,7)
        if Child1 not in exploredNodes:
            visibleNodes.append(Child1)
        if Child2 not in exploredNodes:
            visibleNodes.append(Child2)
    elif(ind == 8):
        Child1 = swap(currentState,8,7)
        Child2 = swap(currentState,8,5)
        if Child1 not in exploredNodes:
            visibleNodes.append(Child1)
        if Child2 not in exploredNodes:
            visibleNodes.append(Child2)
    elif(ind == 1):
        Child1 = swap(currentState,0,1)
        Child2 = swap(currentState,1,2)
        Child3 = swap(currentState,1,4)
        if Child1 not in exploredNodes:
            visibleNodes.append(Child1)
        if Child2 not in exploredNodes:
            visibleNodes.append(Child2)
        if Child3 not in exploredNodes:
            visibleNodes.append(Child3)
    elif(ind == 3):
        Child1 = swap(currentState,0,3)
        Child2 = swap(currentState,3,4)
        Child3 = swap(currentState,3,6)
        if Child1 not in exploredNodes:
            visibleNodes.append(Child1)
        if Child2 not in exploredNodes:
            visibleNodes.append(Child2)
        if Child3 not in exploredNodes:
            visibleNodes.append(Child3)
    elif(ind == 5):
        Child1 = swap(currentState,5,2)
        Child2 = swap(currentState,5,4)
        Child3 = swap(currentState,5,8)
        if Child1 not in exploredNodes:
            visibleNodes.append(Child1)
        if Child2 not in exploredNodes:
            visibleNodes.append(Child2)
        if Child3 not in exploredNodes:
            visibleNodes.append(Child3)
    elif(ind == 7):
        Child1 = swap(currentState,7,6)
        Child2 = swap(currentState,7,8)
        Child3 = swap(currentState,7,4)
        if Child1 not in exploredNodes:
            visibleNodes.append(Child1)
        if Child2 not in exploredNodes:
            visibleNodes.append(Child2)
        if Child3 not in exploredNodes:
            visibleNodes.append(Child3)
    else:
        Child1 = swap(currentState,4,3)
        Child2 = swap(currentState,4,5)
        Child3 = swap(currentState,4,1)
        Child4 = swap(currentState,4,7)
        if Child1 not in exploredNodes:
            visibleNodes.append(Child1)
        if Child2 not in exploredNodes:
            visibleNodes.append(Child2)
        if Child3 not in exploredNodes:
            visibleNodes.append(Child3)
        if Child4 not in exploredNodes:
            visibleNodes.append(Child4)
            
    return visibleNodes,fringeNodes
    
    
            
        
    
    

def BFS(InitialState,GoalState):
    if(GoalTest(InitialState,GoalState)):
        return True; 
    
    fringeNodes = []
    fringeNodes.append(InitialState)
    visibleNodes = []
    exploredNodes = []
    
    while (len(fringeNodes) != 0):
        currentState = fringeNodes.pop(0)
        visibleNodes,fringeNodes=generateChildren(currentState,fringeNodes,visibleNodes,exploredNodes)
        for item in visibleNodes:
            if(GoalTest(item,GoalState)):
                return True;
        exploredNodes.append(currentState)
    return False
    



if __name__ == "__main__":
    InitialState = [1,2,3,4,-1,5,7,8,6]
    
    '''
    
    |  1  |  2  |  3  |
    |  4  |  5  |  B  |
    |  7  |  8  |  6  |
    
    '''
    
    GoalState = [1,2,3,4,5,6,7,8,-1]
    
    '''
    
    |  1  |  2  |  3  |
    |  4  |  5  |  6  |
    |  7  |  8  |  B  |
    
    '''
    flag = BFS(InitialState,GoalState)
    
    if flag == True:
        print("Path Found!")
    else:
        print("Path Not Found!")
        