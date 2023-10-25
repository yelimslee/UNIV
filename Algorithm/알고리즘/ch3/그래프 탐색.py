# 깊이 우선 탐색(dfs) 순환
def dfs(graph, start, visited):
    if start not in visited:
        visited.add(start)
        print(start, end=' ')  # start를 방문했다고 출력
        nbr = graph[start] - visited  # 인접정점-방문정점
        for v in nbr:
            dfs(graph, v, visited)

# 정점의 수 n, 간선의 수 e 
# 그래프가 인접 리스트로 표현되어 있다면, O(n+e)
# 그래프가 인접 행렬로 표현되어 있다면, O(n²)




# 너비 우선 탐색(bfs) 반복
# 큐 구조
import queue
def bfs(graph, start):
    visited = {start}
    que = queue.Queue
    que.put(start)
    while not que.empty():
        v = que.get()
        print(v, end ='')
        nbr = graph[v] - visited  # 인접정점-방문정점
        for u in nbr:
            visited.add(u)
            que.put(u)

# 시작정점 visited에 넣음-> 시작 정점 큐에 넣음-> (큐가 빌때까지)
# -> 큐에서 하나의 정점 v를 꺼냄-> 출력-> {인접정점-방문정점} 
# -> visited에 추가 -> 큐에서 꺼냄

# 그래프가 인접 리스트로 표현되어 있다면, O(n+e)
# 그래프가 인접 행렬로 표현되어 있다면, O(n²)