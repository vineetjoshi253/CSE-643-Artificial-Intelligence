import copy
import time 

PATH = []
OPEN = []
CLOSED = []

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

         
def GoalTest(State,GoalState,n):
    count=0
    for item in range(n+1):
        if State[item] == GoalState[item]:
            count+=1
    return (count == n+1)

def swapState(CurrentState,ind1,ind2):
    tempState = copy.deepcopy(CurrentState)
    temp = tempState[ind1]
    tempState[ind1] = tempState[ind2]
    tempState[ind2] = temp
    return tempState

def unExplored(Child,n):
    global OPEN
    global CLOSED
    for item in CLOSED:
        count = 0
        for i in range(n+1):
            if item[i] == Child[i]:
                count+=1
        if count == n+1:
            return False
        
    for item in OPEN:
        count = 0
        for i in range(9):
            if item[i] == Child[i]:
                count+=1
        if count == n+1:
            return False
    return True

def generateChilds(CurrentState,GoalState,n):
    global OPEN
    global CLOSED 
    CHILDREN = []
    ind = 0 
    for i in range(n+1):
        if CurrentState[i] == -1:
            ind = i
            break
    
    width = int((n+1)**0.5) 
    if ind - width >= 0 :
        Child = swapState(CurrentState,ind,ind -width)
        Child[n+1].append('U')
        if unExplored(Child,n):
            CHILDREN.append(Child)
    
    
    if ind - 1 >= 0 and int(ind/width) == int((ind-1)/width):
        Child = swapState(CurrentState,ind,ind -1)
        Child[n+1].append('L')
        if unExplored(Child,n):
            CHILDREN.append(Child)
        
        
        
    if ind + 1 <= n and int(ind/width) == int((ind+1)/width):
        Child = swapState(CurrentState,ind,ind +1)
        Child[n+1].append('R')
        if unExplored(Child,n):
            CHILDREN.append(Child)
    
    if ind + width <= n:
        Child = swapState(CurrentState,ind,ind +width)
        Child[n+1].append('D')
        if unExplored(Child,n):
            CHILDREN.append(Child)
    
    for i in range(len(CHILDREN)-1,-1,-1):
        OPEN.insert(0, CHILDREN[i])
    
        
def DFS(InitialState,GoalState,n):
    global OPEN
    global PATH
    global CLOSED
          
    OPEN.append(InitialState)
    while(len(OPEN)!=0):
        CurrentState = OPEN.pop()
        if GoalTest(CurrentState,GoalState,n):
            PATH = CurrentState[n+1]
            return True
        generateChilds(CurrentState,GoalState,n)
        CLOSED.append(CurrentState)
    
    return False



if __name__ == "__main__":
    InitialState = []
    n = int(input("Enter The Value Of N :"))
    print("Enter The Initial State With -1 For Blank :")
    InitialState = [int(x) for x in input().split()]
    GoalState = []
    for i in range(n):
        GoalState.append(i+1)
    GoalState.append(-1)
    
    if isSolvable(InitialState,n):
        InitialState.append([])
        start_time = time.perf_counter()
        flag = DFS(InitialState,GoalState,n)
        end_time = time.perf_counter()
        if flag:
            print("PATH FOUND")
            print("Expanded Nodes: ",len(CLOSED),sep="")
            print("Total Saved Nodes: ",len(CLOSED)+len(OPEN),sep="")
            print("Time Taken (In Seconds): ",end_time-start_time,sep="")
            print(PATH)
        else:
            print("UNABLE TO FIND ANY PATH")
    else:
        print("NOT SOLVABLE")
            
        
        
        