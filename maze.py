from random import shuffle, randrange, random
import math

MAZE_SIZE = 10

def DFS_search(g,start_node,end_node):    

    for vertex in g[start_node]:
        explored = []
        path = []
        discovery = []
        explored.append(start_node)
        path.append(start_node)
        if vertex not in explored:
            if vertex == end_node:
                path.append(vertex)
                return path
            discovery.append(vertex)
            
        for adj in discovery:
            DFS_search(g,adj,end_node)
            
    return []


def BFS_search(g,start_node,end_node): 
    L = [] #empty list
    crossedge = []
    explored = []
    explored.append(start_node)
    L.append(start_node)
    i = 0
    while L != 0:
        templist = []
        for e in g[i]: #for each edge incident to v
            if end_node == e: #found end node incident to current vertex, return
                L.append(e)
                return L
            if i not in explored: #if edge e is unexplored
                if e not in explored: #if vertex is unexplored 
                    explored.append(e)
                    L.append(e)
                    templist.append(e) #insert e in templist
                if e in explored: #label e as cross edge
                    crossedge.append(e)
                        
        i += 1
                    
                    
    return []

 
def make_maze():
    vis = [[0] * MAZE_SIZE + [1] for _ in range(MAZE_SIZE)] + [[1] * (MAZE_SIZE + 1)]
    ver = [["|:"] * MAZE_SIZE + ['|'] for _ in range(MAZE_SIZE)] + [[]]
    hor = [["+-"] * MAZE_SIZE + ['+'] for _ in range(MAZE_SIZE + 1)]
 
    def walk(x, y):
        vis[y][x] = 1
 
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+ "
            if yy == y: ver[y][max(x, xx)] = " :"
            walk(xx, yy)
 
    walk(randrange(MAZE_SIZE), randrange(MAZE_SIZE))
 
    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    
    s_temp = s
    graph = [[] for i in range(MAZE_SIZE*MAZE_SIZE)]
    for col in range(MAZE_SIZE):
        for row in range(MAZE_SIZE):
            if s_temp[(2*row+1)*(2*MAZE_SIZE+2)+(2*col)] == " " or (random() < 1/(2*MAZE_SIZE) and col != 0): 
                graph[col+MAZE_SIZE*row].append(col-1+MAZE_SIZE*row)
                graph[col-1+MAZE_SIZE*row].append(col+MAZE_SIZE*row)
                
            if s_temp[(2*row+2)*(2*MAZE_SIZE+2)+(2*col)+1] == " " or (random() < 1/(2*MAZE_SIZE) and row != MAZE_SIZE-1): 
                graph[col+MAZE_SIZE*row].append(col+MAZE_SIZE*(row+1))
                graph[col+MAZE_SIZE*(row+1)].append(col+MAZE_SIZE*row)
    
    return s,graph
 
   
def print_maze(g, path, players):
      
    s = ""
    for col in range(MAZE_SIZE): s+="+---"
    s+="+\n"
    
    for row in range(MAZE_SIZE): 
        s+="|"
        for col in range(MAZE_SIZE): 
            if row*MAZE_SIZE+col == players[0]: s+="👨 "
            elif row*MAZE_SIZE+col == players[1]: s+="🍒 "
            elif row*MAZE_SIZE+col in path: 
                ind = path.index(row*MAZE_SIZE+col)
                if path[ind+1] == row*MAZE_SIZE+col+1: s+=" → "
                elif path[ind+1] == row*MAZE_SIZE+col-1: s+=" ← "
                elif path[ind+1] == row*MAZE_SIZE+col+MAZE_SIZE: s+=" ↓ "
                elif path[ind+1] == row*MAZE_SIZE+col-MAZE_SIZE: s+=" ↑ "
                else: s+="ppp"
            else: s+="   " 
            if (row*MAZE_SIZE+col+1) in g[row*MAZE_SIZE+col]: s+=" "
            else: s+="|"
                
        s+="\n+" 
        for col in range(MAZE_SIZE): 
            if ((row+1)*MAZE_SIZE+col) in g[row*MAZE_SIZE+col]: s+="   +"
            else: s+="---+"
        s+="\n"
        
        
    print(s)
                
    
    
s, g = make_maze()    
players = [0,MAZE_SIZE*MAZE_SIZE-1]
print(g)

print("\n\n ******** PERFORMING DFS ********" )
path_DFS = DFS_search(g,players[0],players[1])
print_maze(g,path_DFS,players)
print("Path length for DFS is %i" % (len(path_DFS)-1))

print("\n\n ******** PERFORMING BFS ********" )
path_BFS = BFS_search(g,players[0],players[1])
print_maze(g,path_BFS,players)
print("Path length for BFS is %i" % (len(path_BFS)-1))