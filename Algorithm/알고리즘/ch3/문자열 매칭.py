# 길이가 n인 문자열 T와 길이가 m인 문자열 P가 있다. T에서 가장 먼저 나타나는 P의 위치를 찾아라.
# 패턴이 없으면 -1을 반환하라

# 텍스트의 첫 번째 문자 위치에 패턴을 놓고 비교한다. 
# 이 과정을 패턴을 오른쪽으로 한 칸씩 옮기면서 성공한 매칭이 나타날 때까지 반복한다.

def string_matching(T, P):
    n = len(T)
    m = len(P)
    for i in range(n-m+1):
        j = 0
        while j<m and P[j]==T[i+j]:  # 기본연산
            j = j+1
        if j == m:
            return i
    return -1

# 입력의 크기: n, m
# 기본연산: P[j]==T[i+j]
# 입력 구성에 따라 성능의 차이가 있음. 
# 최선: O(m) 최악: O(nm)