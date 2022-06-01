import random
import print_tree
from AVL_tree import *

# 1st step
print("\n\n ******************* 1st STEP: search node *******************")
# code that creates the same tree as in the lecture nodes on AVL trees
N54 = Node(1,None,None,54)
N39 = Node(1,None,None,39)
N24 = Node(1,None,None,24)
N71 = Node(1,None,None,71)
N45 = Node(2,N39,N54,45)
N6  = Node(2,None,N24,6)
N67 = Node(3,N45,N71,67)
N33 = Node(4,N6,N67,33)
my_AVL_tree = AVL_tree(N33)
print_tree.print_tree(my_AVL_tree)

# code that searches node 54 (in order to test the search_node function)
print("searching " + str(54) + " ... " ,end="")
stack= my_AVL_tree.search_node(54)
print(stack)
if stack == []: print("ERROR: empty list returned by search_node")
elif stack == None: print("ERROR: None returned by search_node")
elif stack[-1][0]!= None: 
    print("found this: ",end="")
    print(stack[-1][0].key)
    print("Here is the path to find it: ")
    for i in stack: print("[" +str(i[0].key)+ " , " +i[1]+ "]")
    if stack[0][0].key != 33 or stack[0][1] != 'o': print("ERROR: wrong output of search_node function")
    if stack[1][0].key != 67 or stack[1][1] != 'r': print("ERROR: wrong output of search_node function")
    if stack[2][0].key != 45 or stack[2][1] != 'l': print("ERROR: wrong output of search_node function")
    if stack[3][0].key != 54 or stack[3][1] != 'r': print("ERROR: wrong output of search_node function")
else: print("ERROR: found nothing :-/")
print("")

# code that searches node 55 (in order to test the search_node function)
print("\nsearching " + str(55) + " ... " ,end="")
stack= my_AVL_tree.search_node(55)
print(stack)


# 2nd step
print("\n\n ******************* 2nd STEP: add node *******************")
# code that adds node 62 (in order to test the add_node function)
print("adding " + str(62))
t = my_AVL_tree.add_node(62)
if t == None: print("ERROR: no node is returned from add_node function")
print_tree.print_tree(my_AVL_tree)
print("")


# 3rd step
print("\n\n ******************* 3rd STEP: remove node *******************")
# code that removes node 24 (in order to test the remove_node function)
print("removing " + str(24))
t = my_AVL_tree.remove_node(24)
if t == None: print("ERROR: no node is returned from remove_node function")
print_tree.print_tree(my_AVL_tree)
print("")


# 4th step
print("\n\n ******************* 4th STEP: general test *******************")
# code that randomly adds and removes nodes in the AVL tree (to test that all is working fine)
my_AVL_tree = AVL_tree(None)
L = []
for j in range(3):
    for i in range (10): 
       v = random.randint(0,99)
       print("adding " + str(v),end="")
       if my_AVL_tree.add_node(v) != None:
            L.append(v)
       print_tree.print_tree(my_AVL_tree)
    
    for i in range(2):
        if len(L)>1:
            v = random.randint(0,len(L)-1)
        else: 
            print("Empty tree, can't remove a node !")
            break
        print("removing " + str(L[v]),end="")
        if my_AVL_tree.remove_node(L[v]) != None:
            L.remove(L[v])   
        print_tree.print_tree(my_AVL_tree)
