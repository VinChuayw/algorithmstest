import random 
import time
import math

# this function checks if two tasks are conflicting. It assumes L is sorted according to starting time
def is_conflict(L):
    for i in range(len(L)-1):
        if L[i][1] > L[i+1][0]: return True
    return False

# this function makes a random search for assignments
def random_search(L):
    vec_assignment = [0]*len(L)    
    while True:         
        non_conflicting_tasks = []
        for i,el in enumerate(L):
            if vec_assignment[i] == 0:
                vec_assignment[i] = 1
                assignment = [L[k] for k in range(len(L)) if vec_assignment[k]==1 ]
                if not is_conflict(assignment):
                    non_conflicting_tasks.append(i)
                vec_assignment[i] = 0                        
        if len(non_conflicting_tasks)==0:
            assignment = [L[k] for k in range(len(L)) if vec_assignment[k]==1 ]
            val = sum([k[2] for k in assignment])
            print(vec_assignment)
            print(val, assignment)
            return (val,assignment)        
        i = non_conflicting_tasks[random.randint(0,len(non_conflicting_tasks)-1)]
        vec_assignment[i] = 1            

# this function makes a brute force search for assignments
def brute_force(L):    
    n = 2 ** (len(L))
    tasks = [] #temp list for current task set
    non_conflicting_tasks = [] #best combination of tasks
    tempval = 0 #temp benefit for current task set
    val = 0 #best benefit obtained
    for i in range(0, n):
        if len(L) == 10:
            binary = format(i, '010b')  
        if len(L) == 20:
            binary = format(i, '020b') 
        for b in range(0,len(binary)):
            if binary[b] == '1': #set a combination of tasks from L
                tasks.append(L[b])                       
        if len(tasks) > 1: #for combinations with more than 1
            if is_conflict(tasks) == True: #conflict present, break
                tasks = []
                tempval = 0
                continue                    
        for c in range(0,len(tasks)): #summation of benefit
            tempval += tasks[c][2]           
        if tempval > val: #update max benefit if needed            
            val = tempval
            non_conflicting_tasks = tasks.copy()
            tasks = []
            tempval = 0
            continue
        tasks = []
        tempval = 0
        continue         
    return (val, non_conflicting_tasks)

# this function makes a greedy force search for assignments, non-optimal
def greedy(L):
    #choose by order of biggest benefit
    tasks = [] #temp list for current task set
    non_conflicting_tasks = [] #best combination of tasks
    val = 0
    tempval = 0
    L.sort(reverse = True, key = lambda L: L[2]) #sort by biggest benefit
    while True: #eliminate tasks which conflict task with biggest benefit
        for i in range(0, len(L)):
            tasks.append(L[i])            
            for j in range(0, len(L)): #choose tasks to combine
                if L[j] not in tasks: #prevent duplicate value
                    tasks.append(L[j])
                    if is_conflict(tasks) == True: #check for conflict
                        tasks.remove(tasks[-1])                        
            for c in range(0,len(tasks)): #summation of benefit
                tempval += tasks[c][2] 
            if tempval > val:
                val = tempval
                non_conflicting_tasks = tasks.copy()
                tasks = []
                tempval = 0 
            tasks = []
            tempval = 0           
        return (val,non_conflicting_tasks)

# this function makes a dynamic programing search for assignments, can be recursive, optimal
def dynamic_prog(L):
    #sort by end time
    L.sort(key = lambda L: L[1])    
    
    #recursive search for comapring biggest benefit
    for i in range(1,len(L)):
        left = array_search(L[:i-1])
        right = array_search(L[:i])
        if left[0] > right[0]:
            val = left[0]
            non_conflicting_tasks = left[1]
        if right[0] > left[0]:
            val = right[0]
            non_conflicting_tasks = right[1]

    return (val,non_conflicting_tasks)


#searches for the best set of tasks in first i elements
def array_search(L):
    n = len(L)
    if n == 0:      
        tasks = [0,0,0]
        tempval = 0
        return (tempval, tasks)
    if n == 1:
        D = []
        tasks = D.append(L[0])
        tempval = L[0][2]
        return (tempval, tasks)
    else:
        D = []
        D.append(L[-1])
        K = []
        #search for biggest task set backwards
        for i in reversed(range(1,n)):
            if L[i-1][1] < L[-1][0]:
                K.append(L[i-1])
            else:
                continue
        K.sort(key = lambda L: L[2])
        if K != []:
            for c in range(0,len(K)):
                D.append(K[c])
                D.sort(key = lambda L: L[1])
                if is_conflict(D) == True:
                    D.remove(K[c])
                if is_conflict(D) == False:
                    continue

        D.sort(key = lambda D: D[1])    
        tasks = D.copy()
        tempval = 0
        for a in range(0,len(D)):
            tempval += D[a][2]
        return (tempval,tasks)


# this function prints the taskes
def print_tasks(L):
    for i,t in enumerate(L):
        print("task %2i (b=%2i):" %(i,t[2]),end="")
        print(" "*round(t[0]/10) + "-"*round((t[1]-t[0])/10))
        

# this function tests and times a telescope tasks assignment search
def test_telescope(algo,my_tab,display):
    tab = my_tab.copy()
    print("testing",algo,str(" "*(14-len(algo))),"... ",end='')
    t = time.time()
    (max_temp,assignment_temp) = eval(algo + "(tab)")
    print("done ! It took {:.2f} seconds".format(time.time() - t))
    if max_temp!=None:
        print("Solution with benefit = %i" %(max_temp),end='\n')
    if display: 
        if assignment_temp!=None:
            print_tasks(assignment_temp)
            print()
    

MAX_BENEFIT = 99
MAX_START_TIME = 500
MAX_DURATION = 250

NUMBER_OF_ELEMENTS = 10
print("\n ******** Testing to solve for %i events ********" %(NUMBER_OF_ELEMENTS))
val = [(random.randint(1, MAX_START_TIME),random.randint(1, MAX_DURATION),random.randint(1, MAX_BENEFIT)) for i in range(NUMBER_OF_ELEMENTS)] 
tab = sorted([(val[i][0],val[i][0]+val[i][1],val[i][2]) for i in range(NUMBER_OF_ELEMENTS)])
print("Problem instance: ")
print_tasks(tab)
print("")
test_telescope("random_search",tab,True)
test_telescope("brute_force",tab,True)
test_telescope("greedy",tab,True)
test_telescope("dynamic_prog",tab,True)


NUMBER_OF_ELEMENTS = 20
print("\n ******** Testing to solve for %i events ********" %(NUMBER_OF_ELEMENTS))
val = [(random.randint(1, MAX_START_TIME),random.randint(1, MAX_DURATION),random.randint(1, MAX_BENEFIT)) for i in range(NUMBER_OF_ELEMENTS)] 
tab = sorted([(val[i][0],val[i][0]+val[i][1],val[i][2]) for i in range(NUMBER_OF_ELEMENTS)])
test_telescope("random_search",tab,False)
test_telescope("brute_force",tab,False)
test_telescope("greedy",tab,False)
test_telescope("dynamic_prog",tab,False)

