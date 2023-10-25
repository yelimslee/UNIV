# 정렬된 리스트에서의 탐색문제
# 리스트 n개의 항목이 들어있다. 이 리스트에서 "탐색키"를 가진 항목을 찾아라.
# 단, 리스트의 항목들은 정렬되어 있다.


# 순환
def binary_search(A, key, low, high):
    if (low <= high):
        mid = (low + high) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return binary_search(A, key, low, mid-1)
        else:
            return binary_search(A, key, mid+1, high)
    return -1


# 반복
def binary_search_iter(A, key, low, high):
    while (low <= high):
        mid = (low + high) // 2
        if key == A[mid]:  # 기본연산
            return mid
        elif key > A[mid]:
            low = mid+1
        else:
            high = mid-1
    return -1


# 입력의 구성에 따라 시간복잡도가 달라짐
# 최선: O(1)
# 최악: O(log₂n)