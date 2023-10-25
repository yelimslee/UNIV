# xⁿ을 계산하라 

# 반복 (억지기법)  O(n)
def slow_power(x, n):
    result = 1.0
    for i in range(n):
        result = result * x
    return result

# 순환 (축소정복기법)   짝수일 때와 홀수일 때를 나누어 구현   O(log₂n)
def power(x, n):
    if n == 0:
        return 1
    elif (n%2) == 0:  
        return power(x*x, n//2)
    else: 
        return x * power(x*x, (n-1)//2)
