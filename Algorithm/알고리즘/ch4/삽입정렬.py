# 반복
def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i-1
        while j>=0 and A[j]>key:  # 기본연산
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key


# 삽입 정렬의 복잡도는 입력 자료의 구성에 따라 달라짐
# 최선의 경우: O(n) / 이미 오름차순으로 정렬되어 있는 경우
# 최악의 경우: O(n²) / 역으로 정렬된 경우 
# 평균적인 경우: O(n²)
# 안정적이다

# 삽입정렬은 많은 항목을 이동해야 하므로 레코드의 크기가 큰 경우에 효율적이지 않다
# 레코드의 크기가 작은 경우에는 효과적이다. 
# 쉘 정렬도 있음





# 순환
def insertion_sort_recur(A, n):
    if n <= 1:
        return 
    
    insertion_sort_recur(A, n-1)
    key = A[n-1]
    j = n-2
    while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        j = j-1
    A[j+1] = key

# O(n²)