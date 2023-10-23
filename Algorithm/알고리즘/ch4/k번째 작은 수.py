# 리스트에서 k번째로 작은 항목을 찾아라. 단, 리스트는 정렬되어 있지 않다.


# (1)정렬을 이용한 k번째 작은 수 찾기
def kth_smallest_sort(A, k):
    A.sort()
    return A[k-1]

# 선택/삽입 정렬하는 건 O(n²), 인덱스를 꺼내는 건 O(1) => O(n²)
# 퀵/병합 정렬하는 건 => O(nlog₂n)





# 퀵정렬 (가변적인 크기로 문제의 크기가 줄어드는 축소 정복 알고리즘)

# 전체 알고리즘: quick_select()
def quick_selection(A, left, right, k):
    pos = partition(A, left, right)

    if (pos+1 == left+k):
        return A[pos]
    elif (pos+1 > left+k):
        return quick_selection(A, left, pos-1, k)
    else:
        return quick_selection(A, pos+1, right, k-(pos+1-left))
    
# 분할 알고리즘: partition()  O(n)
def partition(A, left, right):
    low = left + 1
    high = right
    pivot = A[left]
    while (low <= high):  # 역전되지 않는 동안
        while low <= right and A[low] <= pivot:
            low += 1
        while high >= left and A[high] > pivot:
            high -= 1

        if low > high:  # 역전
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left]  # 마지막으로 high와 피벗 항목 교환
    return high

# quick_select() 최선: O(n) 최악: O(n²) 평균: O(n)