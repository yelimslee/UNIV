# 하향식 축소 정복 기법, 순환구조 이용
def factorial_recur(n):
    if n == 1:
        return 1
    else:
        return(n * factorial_recur(n-1))  # 기본연산
    


# 상향식 축소 정복 기법, 반복구조 이용
def factorial_iter(n):
    result = 1
    for k in range(1, n+1):  
        result = result * k  # 기본연산
    return result