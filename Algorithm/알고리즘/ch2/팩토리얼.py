# 순환 O(n)
def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n-1)  # 기본연산
    
# 반복 O(n)
def factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result = result * k  # 기본연산
    return result