from collections import deque
import sys
input=sys.stdin.readline

def bfs():
    global graph,n,m,k,x # 목표거리 k 2, 출발은 x 1.
    root = x

    visiteds = [-1]*(n+1)
    dq = deque([root])
    visiteds[root] = 0

    while dq:
        node = dq.popleft()
        for nei in sorted(graph[node]):
            if visiteds[nei] == -1:
                dq.append(nei)
                visiteds[nei] = visiteds[node]+1
    return visiteds

# 노드수, 엣지수, 목표거리, 출발노드
n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(1, m+1):
    a,b = map(int,input().split())
    graph[a].append(b)

print(*([i for i, v in enumerate(bfs()) if v == k] or [-1]), sep="\n")
