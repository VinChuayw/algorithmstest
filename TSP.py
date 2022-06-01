import matplotlib.pyplot as plt
import time
import numpy as np
import random
import heapq


# displays a MST
def plot_MST(pts,MST):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([x[0] for x in pts], [x[1] for x in pts], "ko")
    for i in range(len(MST)): 
        for j in range(len(MST)): 
            if MST[i][j]!= np.infty: ax.plot([pts[i][0],pts[j][0]], [pts[i][1],pts[j][1]], "bo-")
    ax.title.set_text('Minimum Spanning Tree')
            
# computes the Euclidean distance between two points p1 and p2
def euclidean_distance(p1, p2):
    return np.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

# computes the length of a TSP solution
def compute_sol_length(graph,solution):
    length = 0
    for i in range(len(solution)-1): length = length + graph[solution[i]][solution[i+1]]
    return length

# computes with random method the TSP solution
def TSP_random(graph):
    return list(np.random.permutation(len(graph))) 
    
# computes with closest neighbor method the TSP solution
def TSP_closest_neighbor(graph): 
    sol = []
    startint = random.randint(0,len(pts))
    sol.append(startint)
    while len(sol) < len(graph):
        array = graph[startint]
        nextdist = 99999
        nextint = 0
        for item in range(0,len(array)):
            if item not in sol:
                if array[item] != 0:
                    if array[item] < nextdist:
                        nextdist = array[item]
                        nextint = item
        sol.append(nextint)
        nextint = startint        
    sol.append(startint)
    return sol

# computes the Minimum Spanning Tree
def compute_MST(graph): #Prim
    D = [np.infty for j in range(len(graph))] #distance table
    D[0] = 0
    graph_MST = [] 
    temp = []
    large = 99999
    for index in range(len(graph[0])):
        if graph[0][index] != 0:
            if graph[0][index] < large:
                large = graph[0][index]
                nearest = index
    graph_MST.append((0,nearest))
    temp.append(0)
    temp.append(nearest)
    while len(graph_MST) < len(graph) - 1:
        large = 999999
        for t in temp:
            for k in range(len(graph)):
                if k not in temp:
                    if graph[t][k] != 0:                     
                        if graph[t][k] < large:
                            large = graph[t][k]
                            nearest = (t,k)
                            best = k 
        temp.append(best)                
        graph_MST.append(nearest)
    
    return graph_MST

# computes the preorder walk in the tree corresponding to DFS
def DFS_preorder(graph,start_node):   
    if start_node == 0:
        graph = compute_MST(graph)        
    DFS = [] 
    back = []
    discovery = []
    v = start_node
    if v not in DFS:
        DFS.append(v)
    for m in graph:
        if m[0] == v:
            e = m
            if e not in discovery:
                w = e[1]
                if w not in DFS:
                    discovery.append(e)
                    DFS += DFS_preorder(graph,w)
                else:
                    back.append(e)
    return DFS
                     
# computes with Minimum Spanning Tree the TSP solution
def TSP_min_spanning_tree(graph): 
    MST = compute_MST(graph)
    
    graph_MST = [[]]*len(graph)
    for i in range(len(graph)): graph_MST[i] = [np.infty for j in range(len(graph))] 
    for i in range(len(MST)): 
        graph_MST[MST[i][0]][MST[i][1]] = graph[MST[i][0]][MST[i][1]]
        graph_MST[MST[i][1]][MST[i][0]] = graph[MST[i][1]][MST[i][0]]

    plot_MST(pts,graph_MST)        
    return DFS_preorder(graph_MST,0)

    
    
NUMBER_OF_POINTS = 20

# generates random points and sort them accoridng to x coordinate
pts = []
for i in range(NUMBER_OF_POINTS): pts.append([random.randint(0,1000),random.randint(0,1000)])
pts = sorted(pts, key=lambda x: x[0])

graph = [[]]*NUMBER_OF_POINTS
for i in range(NUMBER_OF_POINTS): graph[i] = [euclidean_distance(pts[i],pts[j]) for j in range(NUMBER_OF_POINTS)]

# computes the TSP solutions
print("Computing TSP solution using random technique ... ",end="")
t = time.time()
TSP_sol_random = TSP_random(graph)
print("done ! \n It took %.2f seconds - " %(time.time() - t),end="")
print("length found: %.2f" % (compute_sol_length(graph,TSP_sol_random)))

print("Computing TSP solution using closest neighbor technique ... ",end="")
t = time.time()
TSP_sol_closest_neighbor = TSP_closest_neighbor(graph)
print("done ! \n It took %.2f seconds - " %(time.time() - t),end="")
print("length found: %.2f" % (compute_sol_length(graph,TSP_sol_closest_neighbor)))

print("Computing TSP solution using Minimum Spanning Tree technique ... ",end="")
t = time.time()
TSP_sol_min_spanning_tree = TSP_min_spanning_tree(graph)
print("done ! \n It took %.2f seconds - " %(time.time() - t),end="")
print("length found: %.2f" % (compute_sol_length(graph,TSP_sol_min_spanning_tree)))


# closes the TSP solution for display if needed
if TSP_sol_random[0] != TSP_sol_random[-1]: TSP_sol_random.append(TSP_sol_random[0])
if TSP_sol_closest_neighbor[0] != TSP_sol_closest_neighbor[-1]: TSP_sol_closest_neighbor.append(TSP_sol_closest_neighbor[0])
if TSP_sol_min_spanning_tree[0] != TSP_sol_min_spanning_tree[-1]: TSP_sol_min_spanning_tree.append(TSP_sol_min_spanning_tree[0])


# displays the TSP solution
if NUMBER_OF_POINTS<100:
    fig = plt.figure()
    ax = fig.add_subplot(221)
    ax.plot([x[0] for x in pts], [x[1] for x in pts], "ko")
    ax.title.set_text('Points')  
    ax = fig.add_subplot(222)
    ax.plot([x[0] for x in pts], [x[1] for x in pts], "ko")
    ax.plot([pts[x][0] for x in TSP_sol_random], [pts[x][1] for x in TSP_sol_random], "ro--")
    ax.title.set_text('TSP Random')
    ax = fig.add_subplot(223)
    ax.plot([x[0] for x in pts], [x[1] for x in pts], "ko")
    ax.plot([pts[x][0] for x in TSP_sol_closest_neighbor], [pts[x][1] for x in TSP_sol_closest_neighbor], "ro--")
    ax.title.set_text('TSP Closest Neighbor')
    ax = fig.add_subplot(224)
    ax.plot([x[0] for x in pts], [x[1] for x in pts], "ko")
    ax.plot([pts[x][0] for x in TSP_sol_min_spanning_tree], [pts[x][1] for x in TSP_sol_min_spanning_tree], "ro--")
    ax.title.set_text('TSP Minimum Spanning Tree')
    plt.show(block=False)
    
    
    


    
