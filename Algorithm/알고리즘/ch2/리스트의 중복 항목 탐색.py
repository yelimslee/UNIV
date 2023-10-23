def unique_elements(A):
    n = len(A)
    for i in range(n-1):  # 맨앞부터 순회
        for j in range(i+1, n):  # 2번째부터 순회
            if A[i] == A[j]:
                return False  # 같은 항목이 있으면 False 반환
    return True  # 같은 항목이 있으면 True 반환

A = [32,14,5,17,23,9,14,16,29]
B = [14,6,7,8,12,15]
print(A, unique_elements(A))
print(A, unique_elements(B))

#[32, 14, 5, 17, 23, 9, 14, 16, 29] False
# [32, 14, 5, 17, 23, 9, 14, 16, 29] True

# 최선의 경우 = O(1)
# 최악의 경우 = O(n²)
# 리스트를 먼저 정렬한 후 순서대로 검사하면 O(nlog₂n)으로 줄일 수 있음