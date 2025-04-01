import sys
import heapq
from collections import deque
# sys.setrecursionlimit(10**9)
input=sys.stdin.readline

def bfs_prim(root:int): 
    global graph, visiteds # 그래프는 (가중치, 출발노드, 도착노드)의 리스트로.
    
    hq = [(0, root)] # BFS용 힙 큐는 (가중치, 출발노드)의 리스트로.
    result = 0

    while hq:
        cost, curr = heapq.heappop(hq)
        
        if visiteds[curr]:
            continue

        visiteds[curr]=True
        result += cost

        for c, nei in graph[curr]: # cost, neighbor
            if not visiteds[nei]:
                heapq.heappush(hq, (c, nei))

    return result

def bfs_prim2(root:int): 
    global graph, visiteds # 그래프는 (가중치, 출발노드, 도착노드)의 리스트로.
    
    hq = [(0, root)] # BFS용 힙 큐는 (가중치, 출발노드)의 리스트로.
    result = 0

    while hq:
        cost, node = heapq.heappop(hq)
        
        if visiteds[node]:
            continue

        visiteds[node]=True
        result += cost

        for c, nei in graph[node]: # cost, neighbor
            if visiteds[nei]:
                continue
            heapq.heappush(hq, (c, nei))

    return result


# 입력 & 세팅
nodes_n, edges_e = map(int,input().split())
graph = [[] for _ in range(nodes_n+1)]
visiteds = [False]*(nodes_n+1)

for _ in range(edges_e):
    src, dst, cost = map(int, input().split())
    graph[src].append((cost, dst)) # src에 (가중치, dst노드)
    graph[dst].append((cost, src)) # dst에 (가중치, src노드)

# 계산 & 출력
print(bfs_prim(1))
# print(bfskruskal())


    
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a == root_b:
        return False
    parent[root_b] = root_a
    return True

def kruskal(): # 가중치가 가장 낮은 간선부터 시작하므로 파라미터가 필요없음
    global graph, nodes_n  

    edges = []
    # 간선 리스트 구성 - 중복 간선 있으면 안되니 u < v인 경우에만 추가
    for u in range(1, nodes_n+1):
        for cost, v in graph[u]:
            if u < v:
                edges.append((cost, u, v))
    edges.sort(key=lambda x: x[0])
    
    # 유니온 파인드 자료구조 초기화
    parent = list(range(nodes_n + 1))
    total_cost = 0
    edge_count = 0

    for cost, u, v in edges:
        if union(parent, u, v):
            total_cost += cost
            edge_count += 1
            # 정점 n개를 연결하면 n-1개의 간선이 선택되면 종료
            if edge_count == nodes_n - 1:
                break

    return total_cost