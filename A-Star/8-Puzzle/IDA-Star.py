import copy
import time
PATH = []
OPEN = []
EVALFUN = []
EXP = 0
UpdateBound = 9999

def SearchBlock(State,n):
    for i in range(n+2):
        if State[i] == -1:
            return i

def isSolvable(State,n):
    width = int((n+1)**0.5)
    inv_count = 0
    for i in range(n+1):
        for j in range(i+1,n+1):
            if State[i] == -1 or State[j] == -1:
                continue
            else:
                if(State[i] > State[j]):
                    inv_count+=1
    
    if width%2!=0:
        if(inv_count%2==0):
            return True
        return False
    else:
        ind = SearchBlock(State,n)
        rowNo = width-int(ind/width)
        if rowNo%2 == 0:
            if inv_count%2 == 0:
                return False
            return True
        else:
            if inv_count%2 == 0:
                return True
            return False

def heuristicDis(State,GoalState,n):
    count=0
    for i in range(n+1):
        if State[i] != GoalState[i]:
            count+=1
    return count

def SORT():
    global OPEN
    global EVALFUN
    TEMP1, TEMP2 = zip(*sorted(zip(EVALFUN, OPEN)))
    OPEN = []
    EVALFUN = []
    OPEN = list(TEMP2)
    EVALFUN = list(TEMP1)
    
def swapState(CurrentState,ind1,ind2):
    tempState = copy.deepcopy(CurrentState)
    temp = tempState[ind1]
    tempState[ind1] = tempState[ind2]
    tempState[ind2] = temp
    return tempState
    
def generateChildren(currentState,GoalState,n,Bound):
    global UpdateBound
    global PATH
    global OPEN
    global EVALFUN
    ind = 0 
    for i in range(n+1):
        if currentState[i] == -1:
            ind = i
            break
        
    width = int((n+1)**0.5)    
    if ind - width >= 0 :
        Child = swapState(currentState,ind,ind -width)
        f = heuristicDis(Child,GoalState,n)+len(Child[n+1])
        if f <= Bound:
            Child[n+1].append(currentState[ind-width])
            EVALFUN.append(f)
            OPEN.append(Child)
        else:
            if f < UpdateBound:
                UpdateBound = f
    
    
    if ind - 1 >= 0 and int(ind/width) == int((ind-1)/width):
        Child = swapState(currentState,ind,ind -1)
        f = heuristicDis(Child,GoalState,n)+len(Child[n+1])
        if f <= Bound:
            Child[n+1].append(currentState[ind-1])
            EVALFUN.append(f)
            OPEN.append(Child)
        else:
            if f < UpdateBound:
                UpdateBound = f
    
        
    if ind + 1 <= n and int(ind/width) == int((ind+1)/width):
        Child = swapState(currentState,ind,ind + 1)
        f = heuristicDis(Child,GoalState,n)+len(Child[n+1])
        if f <= Bound:
            Child[n+1].append(currentState[ind+1])
            EVALFUN.append(f)
            OPEN.append(Child)
        else:
            if f < UpdateBound:
                UpdateBound = f
    
    
    if ind + width <= n:
        Child = swapState(currentState,ind,ind + width)
        f = heuristicDis(Child,GoalState,n)+len(Child[n+1])
        if f <= Bound:
            Child[n+1].append(currentState[ind+width])
            EVALFUN.append(f)
            OPEN.append(Child)
        else:
            if f < UpdateBound:
                UpdateBound = f
    
            
def GoalTest(State,GoalState,n):
    count=0
    for item in range(n+1):
        if State[item] == GoalState[item]:
            count+=1
    return (count == n+1)

def AStar(InitialState,GoalState,n,Bound):
    global OPEN
    global EVALFUN
    global EXP
    global PATH
    InitialState.append([])
    OPEN.append(InitialState)
    EVALFUN.append(heuristicDis(InitialState,GoalState,n)+len(InitialState[n+1]))
    k = 0
    while(len(OPEN)!=0):
        k+=1
        SORT()
        currentState = OPEN.pop(0)
        EVALFUN.pop(0)
        if GoalTest(currentState,GoalState,n):
            PATH = currentState[n+1]
            return True
        EXP+=1
        generateChildren(currentState,GoalState,n,Bound)
    EXP = 0
    return False

def IDAStar(InitialState,GoalState,n):
    global UpdateBound
    Bound = heuristicDis(InitialState,GoalState,n)
    while True:
        flag = AStar(InitialState,GoalState,n,Bound)
        Bound = UpdateBound
        UpdateBound = 9999
        if flag == True:
            return True

if __name__ == "__main__":
    n = int(input("Enter The Value Of N : ")) 
    print("Enter The Initial State")
    InitialState = [int(n) for n in input().split()]
    GoalState = [i+1 for i in range(n)]
    GoalState.append(-1)
    
    if isSolvable(InitialState,n):
        start_time = time.perf_counter()
        flag = IDAStar(InitialState,GoalState,n)
        end_time = time.perf_counter()
        if flag:
            print("PATH FOUND!")
            print("Expanded Nodes: ",EXP,sep="")
            print("Total Saved Nodes: ",len(OPEN), sep="")
            print("Time Taken (In Seconds): ",end_time-start_time,sep="")
            print(PATH)
        else:
            print("No Path Found")
    else:
        print("State Not Solvable! No Path Possible")
    