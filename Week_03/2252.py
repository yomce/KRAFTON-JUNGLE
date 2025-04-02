import sys
from collections import deque

input = sys.stdin.read
data = input().split()

n = int(data[0])  # 학생 수
m = int(data[1])  # 비교 수

# 그래프와 진입차수 배열 초기화
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

# 간선 입력
idx = 2
for _ in range(m):
    a = int(data[idx])
    b = int(data[idx + 1])
    graph[a].append(b)
    indegree[b] += 1
    idx += 2

# 진입차수 0인 노드부터 시작
queue = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

result = []

# 위상 정렬
while queue:
    current = queue.popleft()
    result.append(current)

    for neighbor in graph[current]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            queue.append(neighbor)

# 출력
print(" ".join(map(str, result)))