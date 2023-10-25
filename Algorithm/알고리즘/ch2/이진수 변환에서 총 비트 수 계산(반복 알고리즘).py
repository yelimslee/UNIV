# 반복
def binary_digits(n):
    count = 1
    while n > 1:  
        count += 1
        n = n//2  # 기본 연산
    return count

# 입력 크기: n 
# O(log₂n)

# 순환
def binary_digits(n):
    if n <= 1:  # 기본 연산
        return 1
    else:
        return 1 + binary_digits(n//2)  # 기본연산

# 입력 크기: n 
# O(log₂n)  
# 복잡도 순환 관계식: T(n) = T([n/2]) + 1, for n>1, T(1) = 0
# 연속대치법