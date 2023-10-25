def quick_sort(A, left, right):
    if left < right:
        mid = partition(A, left, right)
        quick_sort(A, left, mid-1)
        quick_sort(A, mid+1, right)

def partition(A, left, right):
    low = left + 1
    high = right
    pivot = A[left]
    while (low <= high):
        while low <= right and A[low] <= pivot:
            low += 1
        while high >= left and A[high] > pivot:
            high -= 1

        if low < high:
            A[low], A[high] = A[high], A[low]
        
    A[left], A[high] = A[high], A[left]
    return high

# 최선: 리스트 분할이 항상 리스트의 가운데에서 이루어지는 상황 
# T(n) = 2T(n.2)+n-1, T(1) = 0    => O(nlog₂n)

# 최악: 리스트가 계속 불균형하게 나누어지는 경우, 이미 정렬된 리스트는 퀵정렬에서 최악의 입력임
# T(n) = T(0)+ T(n-1)+n-1, T(n)=n(n-1)/2    => O(n²)

# 평균: O(nlog₂n)
# 안정성을 유지하지 않음



# 불균형 분할을 완화하기 위해 중간값(median)을 피벗으로 선택.
# 퀵 정렬에서 불균형 분할을 완화하기 위해 리스트의 왼쪽, 오른쪽, 중간의 3개의 항목 중에서 중간값을 피벗으로 선택하는
# 방법(median of three)을 구현하라

# 이 방법은 맨앞, 중간, 끝 중에 가운데값을 피벗으로 하려는 방법
# median_index를 구한 후 피벗으로 (=맨앞 인덱스로)
def median_of_three(a, l, r):
    m = (l+r) // 2
    if ((a[l]<a[m]) and (a[m]<a[r]) or (a[r]<a[m]) and (a[m]<a[l])):
        return m
    elif ((a[m]<a[l]) and (a[l]<a[r]) or (a[r]<a[l]) and (a[l]<a[m])):
        return l
    else:
        return r
        

def partition(A, left, right):
    median_index = median_of_three(A, left, right)  # 메디안 위치 구하기
    A[left], A[median_index] = A[median_index], A[left]

    low = left + 1
    high = right
    pivot = A[left]
    while (low <= high):
        while low <= right and A[low] <= pivot:
            low += 1
        while high >= left and A[high] > pivot:
            high -= 1

        if low < high:
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left]
    return high