import sys
from collections import deque
input=sys.stdin.readline

def bfs(graph: dict, marked: list, initial_node: int):
    global result

    dq = deque([initial_node])
    marked[initial_node] = True
    result += 1

    while True:
        curr = dq.popleft()

        for neighbor in sorted(graph[curr]):
            if marked[neighbor]: continue
            
            marked[neighbor] = True
            result += 1
            dq.append(neighbor)

        if len(dq) == 0: break


# 입력 & 세팅
nodes_count = int(input())
edges_count = int(input())

result = 0

graph = {x:[] for x in range(1,nodes_count+1)}

marked = [False]*(nodes_count+1)

for i in range(1, edges_count+1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 계산 - 항상 1번 컴퓨터가 시작
initial_node = 1
bfs(graph, marked, initial_node)

# 출력
print(result-1)
