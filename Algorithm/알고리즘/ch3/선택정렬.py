# 리스트에 n개의 항목들이 들어 있다. 이들을 키의 순서에 따라 오름차순으로 재배치하라

def selection_sort(A):
    n = len(A)
    for i in range(n-1):  # 처음부터
        least = i
        for j in range(i+1, n):  # 두번째부터
            if (A[j] < A[least]):  # 기본연산
                least = j
        A[i], A[least] = A[least], A[i]

# 입력의 크기: 리스트의 전체 항목 수 n
# 입력 구성에 따른 성능 차이 => 최악,평균,최선 다 똑같음
# O(n²)