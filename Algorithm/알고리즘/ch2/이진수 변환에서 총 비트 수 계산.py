def binary_digits(n):
    count = 1
    while n > 1:  
        count += 1
        n = n//2  # 기본 연산
    return count

# 입력 크기: n 
# O(log₂n)