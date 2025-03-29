import sys
from collections import deque
# sys.setrecursionlimit(10**6)
input=sys.stdin.readline


# DFS의 재귀 버전
def dfs_rcs(graph: dict, marked:list, node: int):
    marked[node] = True

    for neighbor in graph[node]:
        if not marked[neighbor]:
            dfs_rcs(graph, marked, neighbor)


# DFS의 반복 버전            
def dfs_itr(graph: dict, marked:list, initial_node: int):
    stack = [initial_node]
    marked[initial_node] = True

    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if not marked[neighbor]:
                marked[neighbor] = True
                stack.append(neighbor)


# BFS의 반복 버전
def bfs(graph: dict, marked:list, initial_node: int):
    queue = deque([initial_node])
    marked[initial_node] = True

    while True:
        current = queue.popleft()
        
        # for neighbor in graph[current]:
        for neighbor in sorted(graph[current]):
            if not marked[neighbor]:
                marked[neighbor] = True
                queue.append(neighbor)

        if len(queue) == 0: break

            
# 입력 & 세팅
nod_count, edg_count = map(int,input().split())
graph = {x:[] for x in range(1,nod_count+1)}

for i in range(edg_count):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

marked = [False] * (nod_count + 1) # 방문한 노드 마킹하는 배열.
result = 0 # 결과 출력.
 
# 계산
for i in range(1, nod_count+1):
    if not marked[i]:
        dfs_itr(graph, marked, i)
        result += 1

# 출력
print(result)