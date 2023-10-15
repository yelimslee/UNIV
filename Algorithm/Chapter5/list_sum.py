def listSumIter(A): # 리스트의 합 반복
    n=len(A)
    sum=0
    for i in range(n):
        sum+=A[i]
    return sum

def listSumDC(A,low,high) : # 리스트의 합 분할정복
    if low==high:
        return A[low]
    else:
        mid=(low+high)//2
        return listSumDC(A,low,mid)+listSumDC(A,mid+1,high)
    


data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7]    # 입력 리스트
n=len(data)
print('반복     합 : ', listSumIter(data))
print('분합정복 합 : ', listSumDC(data, 0, n-1))

# 연습문제 
def minimum(A, low, high):
    if low == high:
        return A[low]
    else:
        mid = (low + high) // 2
        left_min = minimum(A, low, mid)
        right_min = minimum(A, mid + 1, high)
        return min(left_min, right_min)

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]  # 입력 리스트
n = len(data)
print("최소값:", minimum(data, 0, n - 1))
