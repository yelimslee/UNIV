def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid+1, right)
        merge(A, left, mid, right)   # 병합

# 정렬된 두 리스크의 병합
def merge(A, left, mid, right):
    k = left  # 병합을 위한 임시 리스트의 인덱스
    i = left  # 왼쪽 리스트의 인덱스
    j = mid + 1  # 오른쪽 리스트의 인덱스

    while i <= mid and j <= right:
        if A[i] <= A[j]:  # 기본연산
            sorted[k] = A[i]
            i, k = i+1, k+1
        else:
            sorted[k] = A[j]
            j, k = j+1, k+1

    if i > mid:  # 오른쪽 리스트는 다 복사되고 왼쪽 리스트만 남은 경우
        sorted[k:k+right-j+1] = A[j:right+1]
    else:
        sorted[k:k+mid-i+1] = A[i:mid+1]

    A[left:right+1] = sorted[left:right+1]

# T(n) = 2T(n/2)+n-1, T(1) = 0
# a,b=2 , d=1  # O(nlog₂n)

# 병렬정렬의 특징
# 매우 효율적인 정렬 방법의 하나
# 입력 데이터가 어떻게 이루어져 있는지에 상관없이 동일한 시간에 정렬된다
# 안정성을 만족한다
# 단점: 임시리스트가 필요하다 (메모리 낭비)