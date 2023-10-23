# mxm의 정방향 행렬, Mⁿ을 구하라

def multMat()

def powerMat(x, n):
    if n == 1:
        return x
    elif (n%2) == 0:  # 짝수
        return powerMat(multMat(x,x), n//2)
    else:  # 홀수
        return multMat(x, powerMat(multMat(x,x), (n-1)//2))
    
# O(log₂n)