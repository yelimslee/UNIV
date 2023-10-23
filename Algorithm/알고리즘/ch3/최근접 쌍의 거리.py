# 2차원 평면상에 n개의 점이 있다. 가장 인접한 쌍의 거리를 구하라

# 가능한 모든 점의 쌍(pi,pj)에 대해 거리를 계산하고, 가장 짧은 것을 찾는다.

import math
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def closest_pair(p):
    n = len(p)
    mindist = float("inf")
    for i in range(n-1):  # 처음부터
        for j in range(i+1, n):  # 2번째부터
            dist = distance(p[i], p[j])  # 기본 연산
            if dist < mindist:
                mindist = dist
    return mindist

# 입력의 크기: n
# 입력 구성에 따른 성능 차이 => 최악,평균,최선 다 똑같음
# O(n²)
# 분할 정복 알고리즘으로 하면 시간 복잡도를 줄일 수 있음


#분할

# 띠(strip) 영역 내에서 d보다 작은 최근접 쌍의 거리 찾기
def strip_closest(P, d):
    n = len(P)  # 리스트내의 점의 수
    d_min = d
    P.sort(key = lambda point: point[1])  # y축을 따라 정렬

    for i in range(n):
        j = i+1
        # P[i].y와 P[j].y의 차이가 d_min 이내일 때 까지만 처리
        while j<n and (P[j][1]-P[i][j])<d_min:
            dij = dist(P[i], P[j])
            if dij < d_min:
                d_min = dij
            j+=1
    return d_min

# 최근접 쌍의 거리
def closest_pair_dist(P, n): 
    if n <= 3:			            # 점이 3개 이하이면, brute force로 바로 계산
        return closest_pair(P)  	# 억지기법 알고리즘(알고리즘 3.4) 

    mid = n // 2			# 중앙점을 찾음. P는 현재 x로 정렬되어 있음
    mid_x = P[mid][0] 		# 중앙점의 x좌표 
 
    dl = closest_pair_dist(P[:mid], mid)	# Pl에서 dl 계산
    dr = closest_pair_dist(P[mid:], n-mid)	# Pr에서 dr 계산
    d = min(dl, dr)		# d는 둘 중에서 더 짧은 거리
  
    Pm = []				# 중앙에서 x좌표가 d이내인 점들의 집합 Pm을 만듦
    for i in range(n):	# Pm도 x에 대해 정렬되어 있음
        if abs(P[i][0] - mid_x) < d:  
            Pm.append(P[i]) 

    ds = strip_closest(Pm, d)	# Pm내에서 d보다 작은 최근접쌍 거리 찾기
    return min(d, ds)

# O(nlog₂n)