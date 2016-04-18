import numpy

#This Function is Merge Sort
#Code inspired from interactivePython
def mergesort(A):
    if len(A)>1: #do nothing if the length of the array is 1
        mid = len(A)//2 #divide the array into two portions
        leftHalf = A[:mid]
        rightHalf = A[mid:]
        #recursively do the same thing on each half
        mergesort(leftHalf)
        mergesort(rightHalf)
       
        #these variables are indicies for each array
        i=0
        j=0
        k=0
        #This loop will check if i and j are less than the lengths 
        #of the two respective halves
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                # Set A[k] to be the least element in the left half, then increment i
                A[k]=leftHalf[i]
                i=i+1
            else:
                # Set A[k] to be the least element in right half
                A[k]=rightHalf[j]
                j=j+1
            #Always increment k
            k=k+1
        # This loop will 
        while i < len(leftHalf):
            A[k]=leftHalf[i]
            i=i+1
            k=k+1

        while j < len(rightHalf):
            A[k]=rightHalf[j]
            j=j+1
            k=k+1


#This function is Selection Sort
#Code inspired from the lecture Slides
def selectionsort(A):
    for i in range( len(A) ):
        min = i #set a minimum
        for k in range( i + 1 , len(A) ):
            if A[k] < A[min]: #if A[k] is less than the current min
                min = k #set the new min to be k
        #we then swap the min and min Index
        A[min], A[i] = A[i], A[min]

#This function is Insertion Sort
#Code inspired from the lecture slides                
def insertionsort(A):
    for i in range ( 1, len(A) ): #start at A[1] to A[n]
        j = i
        while (j>0) and A[j-1] > A[j]: #while the previous j is less than current j
            A[j], A[j-1] = A[j-1], A[j] #this swaps A[j] and A[j-1]
            j = j-1
            
myList = [12, 5, 13, 8, 9, 65, 78, 2, 53, 65, 21, 80]
mergesort(myList)
print(myList)
