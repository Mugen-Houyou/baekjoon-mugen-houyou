import sys
from collections import deque
input = sys.stdin.readline

def dfs_recursive(root: int):
    global graph, visiteds
    print(root, end=" ")
    visiteds[root] = True

    for neighbor in sorted(graph[root]):
        if visiteds[neighbor]:
            continue
        visiteds[neighbor] = True
        dfs_recursive(neighbor)

def dfs_iterative(root: int):
    global graph, visiteds
    stk = [root]
    result = []
    
    while stk:
        node = stk.pop()
        
        if visiteds[node]: 
            continue

        visiteds[node] = True
        result.append(node)

        # 스택에 넣을 때는 "역순으로" 추가
        for neighbor in sorted(graph[node], reverse=True):
            if visiteds[neighbor]: 
                continue
            stk.append(neighbor)

    return result
        

def bfs(root: int):
    global graph, visiteds
    dq = deque([root])
    result = []
    
    while dq:
        node = dq.popleft()
        
        if visiteds[node]: 
            continue

        visiteds[node] = True
        result.append(node)

        # 이건 큐라 순서대로 추가.
        for neighbor in sorted(graph[node]):
            if visiteds[neighbor]: 
                continue
            dq.append(neighbor)
    
    return result


def bfs_with_level(root: int):
    global graph, visiteds
    dq = deque([root])
    result = []
    level = 0

    while dq:
        print("CURR. LEVEL:",level)
        for _ in range(len(dq)):
            node = dq.popleft()
            
            if visiteds[node]: 
                continue

            visiteds[node] = True
            result.append(node)

            # 이건 큐라 순서대로 추가.
            for neighbor in sorted(graph[node]):
                if visiteds[neighbor]: 
                    continue
                dq.append(neighbor)
        level += 1
    return result


nodes_count, edges_count, start_node = map(int, input().split())
graph = {i: [] for i in range(1, nodes_count + 1)} # 노드가 1,2,3,4,... 같은 식일 것이라고 가정

for _ in range(edges_count):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향으로 넣자.

visiteds = [[] for _ in range(nodes_count+1)]
print(*dfs_iterative(start_node))
visiteds = [[] for _ in range(nodes_count+1)]
print(*bfs_with_level(start_node))


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
