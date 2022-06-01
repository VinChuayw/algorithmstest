# class that represents a tree node
class Node:
    def __init__(self, height, left, right, key):
        self.height = height
        self.left = left
        self.right = right
        self.key = key



# class that represents an AVL tree
class AVL_tree:
    
    def __init__(self, root):
        self.root = root   
                
    # method that search for a node into the AVL tree
    def search_node(self, value):
        path = []
        #case where value is root
        if self.root.key == value:
            path.append([self.root, 'o'])
            return path        
        #case where tree is empty
        if self == None:
            path.append(['None', 'None'])
            return path
        #cases where tree is not empty, set current node
        curr = self.root
        path.append([self.root, 'o'])            
        while True:             
            #case where value is smaller than current node
            if value < curr.key:
                if curr.left == None:
                    path.append(['None', 'None'])
                    break
                path.append([curr.left, 'l'])
                curr = curr.left
                continue
            #case where value is larger than current node
            if value > curr.key:
                if curr.right == None:
                    path.append(['None', 'r'])
                    break            
                path.append([curr.right, 'r'])
                curr = curr.right
                continue                            
            #case where current node is value
            if value == curr.key:
                break        
        return path                
        
    # method that computes the height of a node t and also detects unbalanced
    # between the left and right childs
    def compute_height(self, t):
        #if root is none
        if t == None:
            return 0
        #t in tree, height = max depth of left/right child of t
        
        #if t has no children
        if t.left == None and t.right == None:
            t.height = 1
            return False
        #if t only has left child 
        #if t.left has any child then t is unbalanced        
        if t.right == None and t.left != None:
            if t.left.left != None or t.left.right != None:
                return True
            return False
        #if t only has right child
        #if t.right has any child then t is unbalanced
        if t.right != None and t.left == None:
            if t.right.left != None or t.right.right != None:
                return True
            return False
        #t has both left and right child
        if t.left != None:
            tleft = t.left
        if t.right != None:
            tright = t.right
            left_height = max()
        #left subtree is unbalanced
        if left_height == -1:
            return True
        right_height = AVL_tree.compute_height(self, t.right)
        #right subtree is unbalanced
        if right_height == -1:
            return True
        #difference in height is more than 1
        if abs(left_height - right_height) > 1:
            return True
        #tree is balanced
        return False
                   
    # method that applies a rotation correction
    def rotation_tree(self,a,z,y,x):           
        #situation one: single right to left rotation
        if z.right == y and y.right == x:
            a.right = y
            z.right = y.left
            y.left = z
            return
        #situation two: single left to right rotation
        if z.left == y and y.left == x:
            a.left = y
            z.left = y.right
            y.right = z
            return
        #situation three: double right to left
        if z.right == y and y.left == x:
            z.right = x.left
            y.left = x.right
            a.right = x
            x.left = z
            x.right = y
            return            
        #situation four: double left to right
        if z.left == y and y.right == x:
            z.left = x.right
            y.right = x.left
            a.right = x
            x.left = y
            x.right = z
            return
        return

    # method that will look for possible unbalances in the tree after a node has been added
    def backtrack_height_from_add(self, path):
        p = -1
        for i in range(len(path)-1,-1,-1):
            if AVL_tree.compute_height(path[p][0]) == True:
                AVL_tree.rotation_tree(path[p-1][0],path[p][0],y,x)
            return
        pass
           
            
    # method that will look for possible unbalances in the tree after a node has been removed
    def backtrack_height_from_remove(self, path):
        pass
    
    
    # method that adds a node into the AVL tree
    def add_node(self, value):
        #if tree is empty
        curr = self.root
        if curr == None:
            self.root = Node(1,None,None,value)
            return         
        print(curr.key)
        while True:             
            #case where value is smaller than current node
            if value < curr.key:
                if curr.left == None:
                    curr.left = Node(0,None,None,value) 
                    #update height of parents
                    path = AVL_tree.search_node(self,curr.left.key)
                    p = -1
                    #node height is not 1
                    if path[p-1][0].height >1:
                        path[p][0].height = path[p-1][0].height - 1
                        return curr.left
                    #node height is 1                    
                    for i in range(len(path)-1,-1,-1):
                        if -p != len(path):
                            if path[p-1][0].height - 1 != path[p][0].height:
                                return curr.left
                        path[p][0].height += 1 
                        p -= 1
                        
                    return curr.left          
                curr = curr.left
                continue
            #case where value is larger than current node
            if value > curr.key:
                if curr.right == None:                    
                    curr.right = Node(0,None,None,value)  
                    #update height of parents
                    path = AVL_tree.search_node(self,curr.right.key)
                    p = -1
                    #node height is not 1
                    if path[p-1][0].height > 1:
                        path[p][0].height = path[p-1][0].height - 1
                        return curr.right
                    #node height is 1                    
                    for i in range(len(path)-1,-1,-1):
                        if -p != len(path):
                            if path[p-1][0].height - 1 != path[p][0].height:
                                return curr.right
                        path[p][0].height += 1  
                        p -= 1
                    return curr.right                         
                curr = curr.right
                continue                            
            #case where current node is value
            if value == curr.key:
                return None
        
    # method that removes a node from the AVL tree
    def remove_node(self, value):
        #if tree is empty
        if self == None:
            return None
        #value not in tree
        path = AVL_tree.search_node(self,value)
        if path[-1][0] == 'None':
            return None
        #node is in tree
        prev = path[-2][0]
        curr = path[-1][0]
        direction = path[-1][1]
        #node has no children
        if curr.right == None and curr.left == None:             
            if direction == 'r':
                prev.right.key = None  
                prev.right = None
                #update height of parents if removed node had height = 1
                if curr.height == 1:
                    p = -1
                    path = AVL_tree.search_node(self,prev.key)
                    for i in range(len(path)-1,-1,-1):
                        path[p][0].height -= 1
                        p -= 1
                return curr
            if direction == 'l':
                prev.left.key = None
                prev.left = None
                #update height of parents if removed node had height = 1
                if curr.height == 1:
                    p = -1
                    path = AVL_tree.search_node(self,prev.key)
                    for i in range(len(path)-1,-1,-1):
                        path[p][0].height -= 1
                        p -= 1
                return curr
        #node has only left child
        if curr.right == None and curr.left != None:
            if direction == 'r':
                prev.right.key = curr.left.key
                prev.right = curr.left
                return curr
            if direction == 'l':
                prev.left.key = curr.left.key
                prev.left = curr.left
                return curr
                
        #node has only right child
        if curr.right != None and curr.left == None:
            if direction == 'r':
                prev.right.key = curr.right.key
                prev.right = curr.right
                return curr
            if direction == 'l':
                prev.left.key = curr.right.key
                prev.left = curr.right
                return curr
        #node has children on both sides
        if curr.right != None and curr.left != None:
            #check for biggest value among left side of current node
            bcounter = 0
            pbcurr = None
            bcurr = curr.left
            while bcurr.right != None:
                pbcurr = bcurr
                bcurr = bcurr.right
                bcounter += 1
            #check smallest value right side of current node
            scounter = 0
            pscurr = None
            scurr = curr.right
            while scurr.left != None:
                pscurr = scurr
                scurr = scurr.left
                scounter += 1
            #replace current node with biggest value among left side
            if bcounter > scounter:
                if direction == 'r':
                    prev.right.key = bcurr.key
                    prev.right = bcurr
                    bcurr.right = Node(1, None, curr.right, curr.right.key)
                    bcurr.left.key = curr.left.key
                    bcurr.left = curr.left
                    bcurr.right.key = curr.right.key
                    bcurr.right = curr.right
                    if pbcurr != None:
                        pbcurr.right.key = None
                        pbcurr.right = None
                        return curr
                    
                if direction == 'l':
                    prev.left.key = bcurr.key
                    prev.left = bcurr
                    bcurr.right = Node(1, None, curr.right, curr.right.key)
                    bcurr.left.key = curr.left.key
                    bcurr.left = curr.left
                    bcurr.right.key = curr.right.key
                    bcurr.right = curr.right
                    if pbcurr != None:
                        pbcurr.right.key = None
                        pbcurr.right = None
                        return curr
            #replace current node with smallest value among right side
            if scounter != 0:
                if direction == 'r':
                    prev.right.key = scurr.key
                    prev.right = scurr
                    scurr.left = Node(1, None, curr.left, curr.left.key)
                    scurr.left.key = curr.left.key
                    scurr.left = curr.left
                    scurr.right.key = curr.right.key
                    scurr.right = curr.right
                    if pscurr != None:
                        pscurr.left.key = None
                        pscurr.left = None
                        return curr
                if direction == 'l':
                    prev.left.key = scurr.key
                    prev.left= scurr
                    scurr.left = Node(1, None, curr.left, curr.left.key)
                    scurr.left.key = curr.left.key
                    scurr.left = curr.left
                    scurr.right.key = curr.right.key
                    scurr.right = curr.right
                    if pscurr != None:
                        pscurr.left.key = None
                        pscurr.left = None
                        return curr
            #worst case, both counter = 0, replace with right side
            if bcounter == 0 and scounter == 0:
                if direction == 'r':                    
                    prev.right.key = scurr.key
                    prev.right = scurr  
                    scurr.left = Node(1, None, curr.left, curr.left.key)
                    scurr.left = curr.left                     
                    return curr
                if direction == 'l':
                    prev.left.key = scurr.key
                    prev.left = scurr
                    scurr.left = Node(1, None, curr.left, curr.left.key)
                    scurr.left = curr.left
                    return curr