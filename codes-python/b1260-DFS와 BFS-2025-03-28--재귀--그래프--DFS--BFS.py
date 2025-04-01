import sys
from collections import deque
input = sys.stdin.readline

def dfs_recursive(root: int):
    global graph, visiteds
    print(root, end=" ")
    visiteds[root] = True

    for neighbor in sorted(graph[root]):
        if not visiteds[neighbor]:
            visiteds[neighbor] = True
            dfs_recursive(neighbor)

def dfs_iterative(root: int):
    global graph, visiteds
    stk = [root]
    
    while stk:
        node = stk.pop()
        
        if visiteds[node]: 
            continue

        visiteds[node] = True
        print(node, end=" ")

        # 스택에 넣을 때는 "역순으로" 추가
        for neighbor in sorted(graph[node], reverse=True):
            if visiteds[neighbor]: 
                continue
            stk.append(neighbor)

def bfs(root: int):
    global graph, visiteds
    dq = deque([root])
    
    while dq:
        node = dq.popleft()
        
        if visiteds[node]: 
            continue

        visiteds[node] = True
        print(node, end=" ")

        # 이건 큐라 순서대로 추가.
        for neighbor in sorted(graph[node]):
            if visiteds[neighbor]: 
                continue
            dq.append(neighbor)


nodes_count, edges_count, start_node = map(int, input().split())
graph = {i: [] for i in range(1, nodes_count + 1)} # 노드가 1,2,3,4,... 같은 식일 것이라고 가정

for _ in range(edges_count):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향으로 넣자.

visiteds = [[] for _ in range(nodes_count+1)]
dfs_iterative(start_node)
print()
visiteds = [[] for _ in range(nodes_count+1)]
bfs(start_node)




def dfs_iterative_old(root: int):
    global graph, visiteds
    stk = [root]
    
    while stk:
        node = stk.pop()
        
        if not visiteds[node]:
            visiteds[node] = True
            print(node, end=" ")

            # 스택에 넣을 때는 "역순으로" 추가
            for neighbor in sorted(graph[node], reverse=True):
                stk.append(neighbor)

def bfs_old(root: int):
    global graph, visiteds
    dq = deque([root])
    visiteds[root] = True

    while dq:
        node = dq.popleft()
        print(node, end=" ")
        
        for neighbor in sorted(graph[node]):
            if not visiteds[neighbor]:
                visiteds[neighbor] = True
                dq.append(neighbor)