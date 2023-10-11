# 선택 정렬(재귀 버전)

def selectionSort(A,n):
    if n>1:
        last=n-1
        k = theLargest(A, last)
        A[k], A[last] =  A[last], A[k]
        selectionSort(A,last)

def theLargest(A, last):
    largest = 0
    for i in range(last+1):
        if A[i] > A[largest]:
            largest = i
    return largest


print("selectionSort test")
A = [35, 24, 16, 21, 4, 72, 23, 9, 23, 14, 58, 12, 0]
print("A[]:	   ", A)
selectionSort(A, len(A))
print("Sorted A[]:", A)
