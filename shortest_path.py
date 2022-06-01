from random import randint
import math
import networkx as nx
import matplotlib.pyplot as plt

nx.__version__
NODES = 8              # defines number of nodes in the graph
EDGES = 16              # defines number of edges in the graph
DIRECTED = True         # defines if the graph is directed or undirected
NEGATIVE_WEIGHT = False # defines if the edges can have negative weight
INFINITY = math.inf     # defines a variable for infinity


# function that implements the Dijkstra's algorithm for single-pair shortest paths
def dijkstra(graph, start_node):    
    D = [INFINITY]*len(graph) #intialisation of D table
    D[0] = 0
    cloud = [False]*len(graph) 
    for i in range(0,len(graph)):
        
        if len(g[i]) == 0: #no closest vertex
            v = []
            continue
        if len(g[i]) == 1:
            v = g[i][0]
        if len(g[i]) > 1: #more than one vertex, select smallest
            v = [0,100]
            for j in range(0, len(g[i])):                
                if g[i][j][1] < v[1]:
                    v = g[i][j]
        cloud[(v[0])] = True
        if i == 0:
            for j in g[0]:                
                D[(j[0])] = j[1]
        for outgoing in g[(v[0])]: #for all outgoing from v    
            if cloud[(outgoing[0])] == False: 
                if D[(v[0])] + outgoing[1] < D[(outgoing[0])]:
                    D[(outgoing[0])] = D[(v[0])] + outgoing[1]                
    return D
    

# function that implements the Floyd-Warshall's algorithm for all-pairs shortest paths
def floyd_warshall(graph):
    D = [[[ INFINITY for i in range(len(graph)) ] for j in range(len(graph)) ] for k in range(len(graph)+1) ]
    for a in range(0, len(graph)):
        for b in range(0, len(graph)):
            if a == b:
                D[0][a][a] = 0
            for c in g[a]:
                if b == c[0]:
                    D[0][a][b] = c[1]
                    break
            else:
                D[0][a][b] = INFINITY

         
    for o in range(0, len(graph)):
        for m in range(0, len(graph)):
            for n in range(0, len(graph)):
                D[o+1][m][n] = min(D[o][m][n], D[o][m][o], D[o][o][n])
    return D[len(graph)][:][:]

    
# function that creates the graph
def make_graph(NUMBER_NODES, NUMBER_EDGES, NEGATIVE_WEIGHT, DIRECTED):
    if NODES*NODES<NUMBER_EDGES: 
        print("Impossible to generate a simple graph with %i nodes and %i edges!\n" %(NUMBER_NODES,NUMBER_EDGES))
        return None
    g = [[] for i in range(NUMBER_NODES)]
    for i in range(NUMBER_EDGES):
        while True:
            start_node = randint(0,NUMBER_NODES-1)
            end_node = randint(0,NUMBER_NODES-1)
            if NEGATIVE_WEIGHT: weight = randint(-20,20)
            else: weight = randint(1,20)
            if (start_node != end_node): 
                found = False
                for j in range(len(g[start_node])): 
                    if g[start_node][j][0] == end_node: found = True
                if not found: break            
        g[start_node].append([end_node, weight])
        if DIRECTED==False: g[end_node].append([start_node, weight])
    return g
 

# function that prints the graph
def print_graph(g, DIRECTED):
    if DIRECTED: G = nx.DiGraph()
    else: G = nx.Graph()
    for i in range(len(g)): G.add_node(i)
    for i in range(len(g)):
        for j in range(len(g[i])): G.add_edge(i,g[i][j][0],weight=g[i][j][1])
    for i in range(len(g)):
        print("from node %02i: " %(i),end="")
        print(g[i])
    try: 
        pos = nx.planar_layout(G)
        nx.draw(G,pos, with_labels=True)
    except nx.NetworkXException:
        print("\nGraph is not planar, using alternative representation")
        pos = nx.spring_layout(G)
        nx.draw(G,pos, with_labels=True)
    if DIRECTED: 
        labels=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels, label_pos=0.3)
    else:
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)



    
print("\n\n ******** GENERATING GRAPH ********" )     
g = make_graph(NODES,EDGES,NEGATIVE_WEIGHT,DIRECTED)
if g==None: raise SystemExit(0)
elif NODES<50 and EDGES<2500:
    plt.figure(1,figsize=(10,10))
    print_graph(g,DIRECTED)

print("\n\n ******** PERFORMING DIJKSTRA ********" )    
D = dijkstra(g,0)
print("Single-Pair Distance Table (from node 0): ",end="")
print(D)

print("\n\n ******** PERFORMING FLOYD WARSHALL ********" )   
D = floyd_warshall(g)
print("All-Pairs Distance Table: \n",end="")
for i in range(len(g)): 
    print("from node %02i: " %(i),end="")
    print(D[i])
