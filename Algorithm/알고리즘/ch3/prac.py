# 5
# n개의 검은 구슬과 n개의 흰 구슬이 무작위로 일렬로 나열되어 있다.
# 이 구슬들을 흰 구슬이 모두 먼저 나오고 이후에 검은 구슬이 나오도록 정렬하려고 한다.
# 이때, 구슬의 이동은 인접한 두 구슬을 교환하는 것만 가능하다.

bChanged = True
while bChanged:
    bChanged = False
    for i in range(1, 2*n):
        if A[i-1]==1 and A[i]==0:
            A[i-1], A[i] = 0, 1
            bChanged = True




# 11
# A로 시작하고 B로 끝나는 부분 문자열의 개수를 구하는 문제
# 예, ADBAAEDBA

# (1)이 문제에 대한 억지 기법 알고리즘을 설계하고 시간복잡도를 계산하라
def count_substr(str, A, B):
    count = 0
    n = len(str)
    for i in range(n-1):
        if str[i] == A:
            for j in range(i+1, n):
                if str[j] == B:
                    count += 1
    return count
# O(n²)

# (2)이 문제에 대한 더 효율적인 알고리즘을 찾아보라
# 1. 모든 A의 위치와 B의 위치를 순서대로 찾음 -> 각각 리스트에 저장
# 2. 각각의 A 위치 이후에 있는 B의 개수를 셈
# 두단계 모두 O(n) 시간이 걸림
# O(n)