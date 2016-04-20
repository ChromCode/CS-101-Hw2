import numpy as np
import timeit
import matplotlib.pyplot as plt

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
        #sortedAlist = mergesort(alist)
        #print(sortedAlist)
    
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

#-------------------------------------
#These are all wrapper functions for timeit

def mergeSortInOrder(A):
    #Create a random numpy array with elements ranging from (0, 999) and a length of A
    aList = np.random.randint(1000, size = A ) 
    inOrderAList = sorted(aList)
    mergesort(inOrderAList)
    pass
    
def mergeSortReverseOrder(A):
#Create a random numpy array with elements ranging from (0, 999) and a length of A
    aList = np.random.randint(1000, size = A )
    reverseAList = sorted(aList, reverse = True)
    mergesort(reverseAList)
    pass
    
def insertionSortInOrder(A):
    #Create a random numpy array with elements ranging from (0, 999) and a length of A
    aList = np.random.randint(1000, size = A )
    inOrderAList = sorted(aList)
    insertionsort(inOrderAList)
    pass
    
def insertionSortReverseOrder(A):
    #Create a random numpy array with elements ranging from (0, 999) and a length of A
    aList = np.random.randint(1000, size = A )
    reverseAList = sorted(aList, reverse = True)
    insertionsort(reverseAList)
    pass
    
def selectionSortInOrder(A):
    #Create a random numpy array with elements ranging from (0, 999) and a length of A
    aList = np.random.randint(1000, size = A )
    inOrderAList = sorted(aList)
    selectoinsort(inOrderAList)
    pass
    
def selectionSortReverseOrder(A):
    #Create a random numpy array with elements ranging from (0, 999) and a length of A
    aList = np.random.randint(1000, size = A )
    reverseAList = sorted(aList, reverse = True)
    selectionsort(reverseAList)
    pass
    
#----------------------------------------
#these for loops will plot sorting times on each algorithm based on input size

#mergesort on a sorted and reverse sorted array

for i in range(100, 10100, 100): #this will run from 100 to 10000, printing and plotting time
    orderedArrayTime = timeit.timeit("mergeSortInOrder({0})".format(str(i)), 
    setup="from __main__ import mergeSortInOrder", number = 1)
    
    reversedArrayTime = timeit.timeit("mergeSortReverseOrder({0})".format(str(i)),
    setup="from __main__ import mergeSortReverseOrder", number = 1)
    plt.plot(i, orderedArrayTime, 'bs' )  #Will plot blue squares as orderedArray
    plt.plot(i, reversedArrayTime, 'g^')  #Will plot green triangles as reversedArray
    plt.title('MergeSort on sorted and reverse sorted')
    
plt.show()

#insertionsort on a sorted and reverse sorted array

for i in range(100, 10100, 100): #this will run from 100 to 10000, printing and plotting time
    orderedArrayTime = timeit.timeit("insertionSortInOrder({0})".format(str(i)), 
    setup="from __main__ import selectionSortInOrder", number = 1)
    
    reversedArrayTime = timeit.timeit("insertionReverseOrder({0})".format(str(i)), 
    setup="from __main__ import selectionSortReverseOrder", number = 1)
    
    plt.plot(i, orderedArrayTime, 'bs' )  #Will plot blue squares as orderedArray
    plt.plot(i, reversedArrayTime, 'g^')  #Will plot green triangles as reversedArray
    plt.title('InsertionSort on sorted and reverse sorted')

plt.show()

#selectionsort on a sorted and reverse sorted array
for i in range(100, 10100, 100): #this will run from 100 to 10000, printing and plotting time
    orderedArrayTime = timeit.timeit("selectionSortInOrder({0})".format(str(i)), 
    setup="from __main__ import selectionSortInOrder", number = 1)
    
    reversedArrayTime = timeit.timeit("selectionSortReverseOrder({0})".format(str(i)),
    setup="from __main__ import selectionSortReverseOrder", number = 1)
    plt.plot(i, orderedArrayTime, 'bs' )  #Will plot blue squares as orderedArray
    plt.plot(i, reversedArrayTime, 'g^')  #Will plot green triangles as reversedArray
    plt.title('SelctionSort on sorted and reverse sorted')

plt.show()

#----------------------------------------
#These compare merge, insertion, and selection sort on one graph

#inOrder Array
for i in range(100, 10100, 100): #this will run from 100 to 10000, printing and plotting time
    mergeTime = timeit.timeit("mergeSortInOrder({0})".format(str(i)), 
    setup="from __main__ import mergeSortInOrder", number = 1)
    
    selectionTime = timeit.timeit("selectionSortInOrder({0})".format(str(i)), 
    setup="from __main__ import selectionSortInOrder", number = 1)
    
    insertionTime = timeit.timeit("insertionSortInOrder({0})".format(str(i)), 
    setup="from __main__ import selectionSortInOrder", number = 1)
    
    plt.plot(i, mergeTime, 'bs' )  #Will plot blue squares as orderedArray
    plt.plot(i, selectionTime, 'g^')  #Will plot green triangles as reversedArray
    plt.plot(i, insertionTime, 'ro')
    
    plt.title('Compare all algorihms on a sorted input')

plt.show()
