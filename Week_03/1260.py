from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for neighbor in graph[v]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

# 입력 받기
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 순서대로 탐색하기 위해 정렬
for g in graph:
    g.sort()

# DFS
visited = [False] * (n + 1)
dfs(graph, v, visited)
print()

# BFS
visited = [False] * (n + 1)
bfs(graph, v, visited)