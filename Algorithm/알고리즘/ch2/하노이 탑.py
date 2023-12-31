def hanoi_tower(n, fr, tmp, to):
    if (n == 1):
        print("원판 1: %s -> %s" %(fr, to))  # 원판 옮김 # 기본연산
    else:
        hanoi_tower(n-1, fr, to, tmp)  # n-1개를 to를 이용해 tmp로
        print("원판 %d: %s -> %s" %(n, fr, to))  # 하나의 원판 옮김 # 기본연산
        hanoi_tower(n-1, tmp, fr, to)  # n-1개를 fr을 이용해 to로

# 입력의 크기: n
# O(2ⁿ)
# 복잡도 함수의 순환 관계식: T(n) = T(n-1) +1 + T(n-1), T(1)=1
# 연속대치법. T(n) = 2ⁿ-1