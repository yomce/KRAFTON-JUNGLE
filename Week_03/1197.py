import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

def kruskal(V, edges):
    parent = [i for i in range(V + 1)]  # 1-based indexing
    edges.sort()

    total_cost = 0
    for cost, a, b in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            total_cost += cost

    return total_cost

# 입력 처리
V, E = map(int, input().split())
edges = []

for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

print(kruskal(V, edges))
