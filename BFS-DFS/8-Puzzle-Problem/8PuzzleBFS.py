import copy
import time
PATH =[] 
Open = []
Closed = []
def isSolvable(State,n):
    if n == 10:
        n -= 1
    inv_count = 0
    for i in range(n):
        for j in range(i+1,n):
            if State[i] == -1 or State[j] == -1:
                continue
            else:
                if(State[i] > State[j]):
                    inv_count+=1
    
    return (inv_count%2 == 0)


def GoalTest(State,GoalState):
    count=0
    for item in range(9):
        if State[item] == GoalState[item]:
            count+=1
    return (count == 9)


def swapState(CurrentState,ind1,ind2):
    tempState = copy.deepcopy(CurrentState)
    temp = tempState[ind1]
    tempState[ind1] = tempState[ind2]
    tempState[ind2] = temp
    return tempState

def unExplored(Closed,Child,Open):
    for item in Closed:
        count = 0
        for i in range(9):
            if item[i] == Child[i]:
                count+=1
        if count == 9:
            return False
        
    for item in Open:
        count = 0
        for i in range(9):
            if item[i] == Child[i]:
                count+=1
        if count == 9:
            return False
    return True

def generateChilds(CurrentState,GoalState,Open,Closed):
    global PATH
    ind = 0 
    for i in range(9):
        if CurrentState[i] == -1:
            ind = i
            break
        
    if ind - 3 >= 0 :
        Child = swapState(CurrentState,ind,ind -3)
        Child[9].append(CurrentState[ind-3])
        if GoalTest(Child,GoalState):
            PATH = Child[9]
            return True
        if unExplored(Closed,Child,Open) and isSolvable(Child,10):
            Open.append(Child)
    
    
    if ind - 1 >= 0 and ind-1!=2 and ind-1!=5:
        Child = swapState(CurrentState,ind,ind -1)
        Child[9].append(CurrentState[ind-1])
        if GoalTest(Child,GoalState):
            PATH = Child[9]
            return True
        if unExplored(Closed,Child,Open) and isSolvable(Child,10):
            Open.append(Child)
        
        
        
    if ind + 1 <= 8 and ind+1 != 3 and ind+1!= 6:
        Child = swapState(CurrentState,ind,ind +1)
        Child[9].append(CurrentState[ind+1])
        if GoalTest(Child,GoalState):
            PATH = Child[9]
            return True
        if unExplored(Closed,Child,Open) and isSolvable(Child,10):
            Open.append(Child)
    
    
    if ind + 3 <= 8:
        Child = swapState(CurrentState,ind,ind +3)
        Child[9].append(CurrentState[ind+3])
        if GoalTest(Child,GoalState):
            PATH = Child[9]
            return True
        if unExplored(Closed,Child,Open) and isSolvable(Child,10):
            Open.append(Child)

def BFS(InitialState, GoalState):
    global PATH
    InitialState.append([])
    if GoalTest(InitialState,GoalState):
        PATH = InitialState[9]
        return True
    else:
        global Open
        global Closed
        Open.append(InitialState)
        
        while(len(Open)!=0):
            CurrentState= Open.pop(0)
            flag = generateChilds(CurrentState,GoalState,Open,Closed)
            if(flag == True):
                return True
            Closed.append(CurrentState)
            
        
        

if __name__ == "__main__":
    InitialState = [1,2,3,4,6,8,7,5,-1]
    GoalState = [1,2,3,4,5,6,7,8,-1]
    
    if isSolvable(InitialState,9):
        start_time = time.perf_counter()
        flag = BFS(InitialState,GoalState)
        end_time = time.perf_counter()
        if flag:
            print("Path Found!")
            print("Expanded Nodes: ",len(Closed),sep="")
            print("Total Saved Nodes: ",len(Closed)+len(Open),sep="")
            print("Time Taken (In Seconds): ",end_time-start_time,sep="")
            print(PATH)
        else:
            print("Not Solvable! No Path Found")
    else:
            print("Not Solvable! No Path Found")