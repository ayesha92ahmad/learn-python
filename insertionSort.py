#insertion sort
def insertionSort(A):
    for j in range(2,len(A)):
        key = A[j]
        i= j-1
        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            i=i-1
        A[i+1] = key
    print A , len(A)

A = [6,3,7,2,8,1,100,54]
insertionSort(A)
