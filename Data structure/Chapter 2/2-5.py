# 선택 정렬(비재귀 버전)

# n개로 이루어진 A 리스트를 정렬
def selectionSort(A,n):
	for last in range(n-1, 0, -1):  # 뒤부터 순회
		k = theLargest(A, last)	
		A[k], A[last] =  A[last], A[k]   # 가장 큰 원소를 찾아 맨 오른쪽 원소와 맞바꿈

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
