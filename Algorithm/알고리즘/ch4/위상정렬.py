# 위상정렬 : 방향 그래프 G=(V,E)가 주어졌다. 
# G에 존재하는 각 정점들의 선행 순서를 위배하지 않으면서 모든 정점들을 순서대로 나열하라.
# 축소 정복 기법

def topological_sort(graph):
    inDeg = {}              	# { 정점:진입차수 } 저장을 위한 공백 딕셔너리
    for v in graph:         	# 그래프의 모든 정점에 대해
        inDeg[v] = 0        	# 0으로 초기화. inDeg = { "A":0, "B":0, ... }
    for v in graph:         	# 모든 정점 v 에 대해
        for u in graph[v]:  	# v에 인접한 모든 정점 u에 대해
            inDeg[u] += 1   	# 진입차수를 1 증가시킴

    vlist = []              	# 진입차수가 0인 정점 리스트를 만듦
    for v in graph:
        if inDeg[v] == 0:		# 진입차수가 0이면 vlist에 추가
            vlist.append(v)

    while vlist:			 	# vlist가 공백이 아닐 때 까지
        v = vlist.pop()
        print(v, end=' ')

        for u in graph[v]:	    # 연결된 정점의 진입차수 감소
            inDeg[u] == -1
            if inDeg[u] == 0:	# 진입차수가 0이면 vlist에 추가
                vlist.append(u)

mygraph = { "A" : {"C", "D"},
            "B" : {"D", "E"},
            "C" : {"D", "F"},
            "D" : {"F"},
            "E" : {"F"},
            "F" : set()
          }

topological_sort(mygraph)
print() # B E A C D F

# 모든 정점의 진입차수를 계산하는 단계: O(n+e)
# 진입차수가 0인 정점 리스트를 만드는 단계: O(n)
# 주 알고리즘: O(e)
# => O(n+e)