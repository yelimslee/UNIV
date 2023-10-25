def find_max(A):
    max = A[0]
    for i in range(len(A)):
        if A[i] > max:  # 기본연산
            max = A[i]
    return max