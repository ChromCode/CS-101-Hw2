import numpy as np

#This Function is Merge Sort
#Code inspired from interactivePython
def mergesort(A):
    if A.size == 1:
        return A
    mid = A.size//2
    leftHalf = A[:mid]
    rightHalf = A[mid:]
    #recursively do the same thing on each half
    lSort = mergesort(leftHalf)
    rSort = mergesort(rightHalf)
    return merge(lSort, rSort) #combine two arrays that are sorted
    #to get the correct sorted output, follow these lines
    #######################################
        #sortedAlist = mergesort(alist)
        #print(sortedAlist)
    #######################################
    
# this code follows the pseudocode from the lecture slides
def merge(B,C):
    D = np.empty([(B.size + C.size)]) #initialize an empty array
    Infinity = float('inf') # this is represented as infinity
    B = np.append(B, Infinity) #append infinity to the end of B and C
    C = np.append(C, Infinity)
    i = j = k = 0
    #while the current element is not infinity, do comparisons on the elements of B and C
    while B[i] < Infinity or C[j] < Infinity: 
        if B[i] < C[j]:
            D[k] = B[i]
            i = i + 1
        else:
            D[k] = C[j]
            j = j + 1
        k = k + 1 # we Always increment k
    return D

#This function is Selection Sort
#Code inspired from the lecture Slides
def selectionsort(A):
    for i in range( A.size ):
        min = i #set a minimum
        for k in range( i + 1 , A.size ):
            if A[k] < A[min]: #if A[k] is less than the current min
                min = k #set the new min to be k
        #we then swap the min and min Index
        A[min], A[i] = A[i], A[min]

#This function is Insertion Sort
#Code inspired from the lecture slides                
def insertionsort(A):
    for i in range ( 1, A.size ): #start at A[1] to A[n]
        j = i
        while (j>0) and A[j-1] > A[j]: #while the previous j is less than current j
            A[j], A[j-1] = A[j-1], A[j] #this swaps A[j] and A[j-1]
            j = j-1
