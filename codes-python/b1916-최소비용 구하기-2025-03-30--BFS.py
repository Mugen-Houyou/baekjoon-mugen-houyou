import sys
import heapq
import math
input=sys.stdin.readline

def bfs_djk():
    global graph, start_n, end_n
    
    dist = [math.inf] * len(graph) 
    dist[start_n] = 0
    hq = [(0, start_n)] 

    while hq:
        acc_cost, curr = heapq.heappop(hq)

        # 현재 cost가 dist[node]보다 크다면, 더 좋은 경로가 이미 발견된 상태
        # 즉 기존 BFS의 visited 리스트와 비슷하게 역할
        if acc_cost > dist[curr]:
            continue

        # 현재 노드의 인접 노드에 대해 완화(relaxation) 수행
        # "완화 (relaxation)"란 최단 경로 알고리즘의 핵심 동작 중 하나.
        # 간단히 말해, 더 짧은 경로를 발견했을 때, 기존 값을 갱신.
        for c, nei in graph[curr]:# cost, neighbor
            # 미방문 & 이 경로가 더 짧다면 갱신
            if acc_cost+c < dist[nei]:
                dist[nei] = acc_cost+c
                heapq.heappush(hq, (dist[nei], nei)) # dist[nei] => 현재까지의 누적 최단 거리
    
    return dist[end_n]


# 입력 & 세팅
n = int(input())  # 노드 수
m = int(input())  # 에지 수
graph = [[] for _ in range(n+1)]
for _ in range(m):
    src, dst, cost = map(int, input().split())
    graph[src].append((cost, dst)) # src에 (가중치, dst노드)
    # graph[dst].append((cost, src)) # 단방향이라 안됨!
start_n, end_n = map(int, input().split())

# 계산 & 출력
print(bfs_djk())

# def bfs_djk():
#     global graph, visiteds, start_n, end_n
   
#     accu_costs = [math.inf]*len(graph) # 각 노드까지의 최단 거리 리스트 (일단 무한대로 초기화)
#     accu_costs[start_n] = 0
#     hq = [(0, start_n)] 

#     while hq:
#         cml_cost, node = heapq.heappop(hq)

#         if visiteds[node]:
#             continue

#         visiteds[node] = True

#         # 현재 노드의 인접 노드에 대해 완화(relaxation) 수행
#         # "완화 (relaxation)"란 최단 경로 알고리즘의 핵심 동작 중 하나.
#         # 간단히 말해, 더 짧은 경로를 발견했을 때, 기존 값을 갱신.
#         for c, nei in graph[node]: 
#             if not visiteds[nei] and cml_cost+c < accu_costs[nei]:
#                 accu_costs[nei] = cml_cost+c
#                 heapq.heappush(hq, (accu_costs[nei], nei)) 
    
#     return accu_costs[end_n] # end_n만


# # 입력 & 세팅
# n = int(input()) # 노드 수 n
# m = int(input()) # 에지 수 m
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     src, dst, cost = map(int, input().split())
#     graph[src].append((cost, dst)) # a에 (가중치, 도착노드)
#     # graph[dst].append((cost, src)) # 단방향이라 안됨!
# visiteds = [False for _ in range(len(graph))]
# start_n, end_n = map(int, input().split())