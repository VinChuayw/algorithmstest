import random 
import time
import math


def bubble_sort(my_list):       
    # do n passes on the list
    swapped = True
    while swapped:
       swapped = False   

	   # check neighbours and swap them if needed     
       for j in range(len(my_list)-1):
           if my_list[j] > my_list[j+1]:
               temp = my_list[j]
               my_list[j] = my_list[j+1]
               my_list[j+1] = temp     
               swapped = True


def selection_sort(my_list):  
    for i in range(len(my_list)-1): # perform n-1 passes
        
    	# find the minimum in the unsorted part of my_list 
        min_index = i
        for j in range(i+1,len(my_list)):
            if my_list[j]< my_list[min_index]:
                min_index = j
            
        # swap this min element with the first unsorted element from my_list 
        temp = my_list[i]
        my_list[i] = my_list[min_index]
        my_list[min_index] = temp 


def insertion_sort(my_list):
    i = 1                   # i is the size of the sorted list
    while i < len(my_list): # while the list is not sorted yet
    	j = i
    
    	# place the element j at the proper place in the sorted list
    	while j > 0 and my_list[j-1] > my_list[j]:
    	  # swap 
    	  temp = my_list[j]
    	  my_list[j] = my_list[j-1]
    	  my_list[j-1] = temp
    	  j = j - 1 
            
    	i = i + 1


def merge_sort(my_list):
    # if the list is empty or contains just one element, no need to sort 
    if len(my_list) <= 1: return my_list
     
    # we divide the work in two halves, and sort them recursively
    mid = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid])      
    right = merge_sort(my_list[mid:])   
    
    # merge the two sorted halves, while keeping the list sorted
    my_sorted_list = []
    while left != [] or right != []: 
        if left == []: my_sorted_list.append(right.pop(0))  # left is empty
        elif right == []: my_sorted_list.append(left.pop(0)) # right is empty
        elif left[0] < right[0]: my_sorted_list.append(left.pop(0))
        else:  my_sorted_list.append(right.pop(0))
    
    return my_sorted_list



def quick_sort(my_list):
    # if the list is empty or contains just one element, no need to sort 
    if len(my_list) <= 1: return my_list
    #divide into two portions, keep list sorted
      
    pivot_index = random.randint(0,len(my_list)-1) 
    pivot = []
    left = []
    right = []
    for x in range(len(my_list)):
        if my_list[x] < my_list[pivot_index]:
            left.append(my_list[x])
        elif my_list[x] > my_list[pivot_index]:
            right.append(my_list[x])
        elif my_list[x] == my_list[pivot_index]:
            pivot.append(my_list[x])
    
    #merge the portions while keeping list sorted
    my_sorted_list = []    
    my_sorted_list.extend(quick_sort(left) + pivot + quick_sort(right))
    
    return my_sorted_list
    
def add_to_heap(heap,element):
    #list format
    #index i has child at indexes 2i + 1 and 2i + 2
    #index i has parent at ceil(i/2) - 1
    heap.append(element)
    m = len(heap)-1 #current index of element
    n = math.ceil(m/2) -1 #index of parent
    if len(heap) > 1:
        while heap[m] < heap[n]:
            heap[m], heap[n] = heap[n], heap[m] 
            m = n
            if m == 0: #element is now smallest, break                        
                break
            n = math.ceil(m/2) -1           
    return heap
    
def remove_min_from_heap(heap):
    element = heap.pop(0)   
    if len(heap) > 1: #insert end of heap to start
        heap.insert(0,heap.pop(-1))
        m = 0  
        l = 2*m + 1 #index of left child
        r = 0
        if len(heap) > 2:
            r = 2*m + 2 #index of right child
        while l <= len(heap)-1:  
           if heap[l] < heap[m]: #has at least one left child
               if r != 0 and r <= len(heap)-1: #has 2 children 
                   if heap[l] <= heap[r]: #l=r or l<r  
                       heap[m], heap[l] = heap[l], heap[m] 
                       m = l
                       l = 2*m + 1
                       r = 2*m + 2
                       continue
                   if heap[l] > heap[r]: #l>r        
                       heap[m], heap[r] = heap[r], heap[m]
                       m = r
                       l = 2*m + 1
                       r = 2*m + 2
                       continue
               #only l exists
               heap[m], heap[l] = heap[l], heap[m] 
               m = l
               l = 2*m + 1
           if r != 0 and r <= len(heap)-1: #case where l>m but r<m
               if heap[r] <= heap[m]:
                   heap[m], heap[r] = heap[r], heap[m]
                   m = r
                   l = 2*m + 1
                   r = 2*m + 2
                   continue           
           break       
    return element

def heap_sort(my_list): 
    heap = []
    my_sorted_list = []
    n = len(my_list)
    #add elements to heap
    for i in range(0,n):
        add_to_heap(heap, my_list[i])        
    #remove from heap to sort
    for i in range(0,n):
        my_sorted_list.append(remove_min_from_heap(heap))
    return my_sorted_list



def test_sorting(algo,my_tab,display):
    tab = my_tab.copy()
    print("testing",algo,str(" "*(14-len(algo))),"... ",end='')
    t = time.time()
    temp = eval(algo + "(tab)")
    if temp != None: tab = temp
    print("done ! It took {:.2f} seconds".format(time.time() - t))
    if display: print(tab,end='\n\n')
    

print("\n ******** Testing to sort a small table of 30 elements ********")
NUMBER_OF_ELEMENTS = 30
tab = [random.randint(1, 40) for i in range(NUMBER_OF_ELEMENTS)] 
#tab = list(set([random.randint(1, 40) for i in range(NUMBER_OF_ELEMENTS)]))
print("Original table: ")
print(tab,end='\n\n')
test_sorting("bubble_sort",tab,True)
test_sorting("selection_sort",tab,True)
test_sorting("insertion_sort",tab,True)
test_sorting("merge_sort",tab,True)
test_sorting("quick_sort",tab,True)
test_sorting("heap_sort",tab,True)

print("\n ******** Testing to sort a big table of 5000 elements ********")
NUMBER_OF_ELEMENTS = 5000
tab = list(set([random.random() for i in range(NUMBER_OF_ELEMENTS)]))
test_sorting("bubble_sort",tab,False)
test_sorting("selection_sort",tab,False)
test_sorting("insertion_sort",tab,False)
test_sorting("merge_sort",tab,False)
test_sorting("quick_sort",tab,False)
test_sorting("heap_sort",tab,False)
