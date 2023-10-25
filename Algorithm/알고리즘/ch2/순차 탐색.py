def sequential_search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return i
    return -1

# 최선의 경우: O(1), 최악의 경우 O(n), 평균의 경우 O((n+1)/2)

# while문
def sequential_search2(A, key):
    n = len(A)
    i = 0
    index = -1
    while i < n and index == -1:
        if A[i] == key:
            index = i
        i += 1
    return index