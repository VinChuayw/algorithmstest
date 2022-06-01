import matplotlib.pyplot as plt
import time
import random


# function that checks if three points a,b,c are clockwise positioned 
def is_clockwise(a,b,c):
    return ((c[1] - a[1]) * (b[0] - a[0])) < ((b[1] - a[1]) * (c[0] - a[0]))    
    
# compute with naive method the convex hull of the points cloud pts 
# and store it as a list of vectors
def convex_hull_2d_gift_wrapping(pts):
    hull = []
    hull.append(pts[0])    
    # make triplet group a,b,c ; a is already part of the hull, b is pending for hull and c is for checking clockwise
    for n in (hull): 
        #set a        
        a = hull[-1]
        #make a temp list which excludes a
        temp = pts.copy()
        temp.remove(a)
        for i in temp:
            #set b
            b = i
            #if next b is already in hull, skip
            if b in hull:
                continue
            #make temp2 which excludes a and b
            temp2 = temp.copy()
            temp2.remove(b)
            for j in temp2:
                #set c
                c = j
                # call is_clockwise to check if the triplet is clockwise
                # if at least one False, check from another value of b and c, otherwise continue
                if is_clockwise(a,b,c) == True:
                    continue
                if is_clockwise(a,b,c) == False:
                    break
            # if all True (all of c are clockwise), add b to hull, set b as new a
            if is_clockwise(a,b,c) == False:
                continue
            hull.append(b)
            break   
    print(hull, 'hull' , len(hull))
    return hull
###complexity of the algorithm is O(n^3)

# compute with divide and conquer method the convex hull of the points  
# cloud pts and store it as a list of vectors
def convex_hull_2d_divide_conquer(pts):
    size = len(pts)
    if size > 7:
        mid = len(pts) // 2
        left = pts[:mid]
        right = pts[mid:]
        
        convex_hull_2d_divide_conquer(left)
        convex_hull_2d_divide_conquer(right)
        
        left = convex_hull_2d_gift_wrapping(left)
        right = convex_hull_2d_gift_wrapping(right)
        hull = []
        print(hull)
        #split halves into left and top
        lefttop = left[:left.index(max(left, key = lambda x: x))+1]
        leftbot = left[left.index(max(left, key = lambda x: x)):]
        leftbot.append(left[0])
        righttop = right[:right.index(max(right, key = lambda x: x))+1]
        rightbot = right[right.index(max(right, key = lambda x: x)):]
        rightbot.append(right[0])
        #form top 
        while True:
            #check left side
            if len(lefttop) > 1 and len(righttop) > 1:
                x = lefttop[-2]
                y = lefttop[-1]
                z = righttop[0]                
                if is_clockwise(x,z,y) == True:
                        lefttop.remove(y)
                        continue
            #check right side
            if len(lefttop) > 1 and len(righttop) > 1:
                x = lefttop[-1]
                y = righttop[0]
                z = righttop[1] 
                if is_clockwise(x,z,y) == True:
                        righttop.remove(y)
                        continue                        
            break
        hull.extend(lefttop + righttop)
        #form bot
        while True:
            #check left side
            if len(leftbot) > 1 and len(rightbot) > 1:
                x = leftbot[1]
                y = leftbot[0]
                z = rightbot[-1]
                if is_clockwise(x,z,y) == False:
                        leftbot.remove(y)
                        continue
            #check right side
            if len(leftbot) > 1 and len(rightbot) > 1:
                x = leftbot[0]
                y = rightbot[-1]
                z = rightbot[-2]
                if is_clockwise(x,z,y) == False:
                        rightbot.remove(y)
                        continue                       
            break
        hull.extend(rightbot + leftbot)
        print(hull, 'hull' , len(hull))
        return hull
#complexity of program is nlog(n)  
    
NUMBER_OF_POINTS = 20

# generate random points and sort them accoridng to x coordinate
pts = []
for i in range(NUMBER_OF_POINTS): pts.append([random.random(),random.random()]) 
pts = sorted(pts, key=lambda x: x[0])



# compute the convex hulls
print("Computing convex hull using gift wrapping technique ... ",end="")
t = time.time()
hull_gift_wrapping = convex_hull_2d_gift_wrapping(pts)
print("done ! It took ",time.time() - t," seconds")

print("Computing convex hull using divide and conquer technique ... ",end="")
t = time.time()
hull_divide_conquer = convex_hull_2d_divide_conquer(pts)
print("done ! It took ",time.time() - t," seconds")

# close the convex hull for display
hull_gift_wrapping.append(hull_gift_wrapping[0])
hull_divide_conquer.append(hull_divide_conquer[0])

# display the convex hulls
if NUMBER_OF_POINTS<1000:
    fig = plt.figure()
    ax = fig.add_subplot(131)
    ax.plot([x[0] for x in pts], [x[1] for x in pts], "ko")
    ax.title.set_text('Points')
    ax = fig.add_subplot(132)
    ax.plot([x[0] for x in pts], [x[1] for x in pts], "ko")
    ax.plot([x[0] for x in hull_gift_wrapping], [x[1] for x in hull_gift_wrapping], "ro--")
    ax.title.set_text('Gift Wrapping')
    ax = fig.add_subplot(133)
    ax.plot([x[0] for x in pts], [x[1] for x in pts], "ko")
    ax.plot([x[0] for x in hull_divide_conquer], [x[1] for x in hull_divide_conquer], "ro--")
    ax.title.set_text('Divide/Conquer')
    plt.show(block=False)


    
