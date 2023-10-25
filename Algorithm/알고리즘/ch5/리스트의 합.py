# 리스트의 합 (반복)
def listSumIter(A):
    n = len(A)
    sum = 0
    for i in range(n):
        sum += A[i]
    return sum

# 리스트의 합 (분할)
def listSumDC(A, low, high):
    if low == high:
        return A[low]
    else:
        mid = (low+high)//2
        return listSumDC(A, low, mid) + listSumDC(A, mid+1, high)