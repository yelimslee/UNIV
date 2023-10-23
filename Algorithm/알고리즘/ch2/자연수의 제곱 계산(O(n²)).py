def computer_square_C(n):  # O(n²)
    sum = 0
    for i in range(n):
        for j in range(n):
            sum = sum + 1  # 기본연산
    return sum