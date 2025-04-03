# 검은 방에서 흰 방으로 바꾸어야 할 최소의 수를 구하는 프로그램을 작성.
import sys
import heapq
from collections import deque
import copy
import pprint

ABOUT_MAX = 1<<31
ABOUT_MIN = -1<<31
input = sys.stdin.readline

def is_within_bounds(r,c):
    global n
    return (0<=r<n) and (0<=c<n)  

def dijk(limit_count: int, current_path_costs: list): # 최대 부술 수 있는 개수, 현재 비용
    global graph,path_costs,result
    
    dq = deque()
    dq.append((0,0))
    last_black_blocks = set()
    path_costs[0][0] = 1
    distance = 0
    djk_pc = copy.deepcopy(current_path_costs) # 비용 2차원 행렬을 복사 뜸
    hit = 0  # hit개째 부수는 중.

    # 탐색
    while dq:
        #r,c = heapq.heappop(dq)
        r,c = dq.popleft()
        
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if (not is_within_bounds(nr,nc) 
                or path_costs[nr][nc] != 0
            ):
                continue
            if graph[nr][nc] == 0:
                last_black_blocks.add((nr,nc))
                continue

            path_costs[nr][nc] = path_costs[r][c]+1
            # heapq.heappush(dq, (nr,nc))
            dq.append((nr,nc))

    # 막혔다면, 벽을 하나 부숴봄
    if hit <= limit_count:
        hit += 1

    return djk_pc


def solve(limit_count: int): # 최대 부술 수 있는 개수
    global graph,path_costs,result
    
    current_path_costs = [[0]*n for _ in range(n)]
    
    i=0
    current_path_costs = dijk(i, current_path_costs)
    while current_path_costs[n-1][n-1] != 0:
        dijk(i, current_path_costs)
        i+=1

    return i


    # 다시 탐색

    # 또 막혔다면, 저거 말고 다른 벽을 부숴봄

    # ... end가 0이 아닐 때까지 반복

    

    pprint.pprint(path_costs)
    pprint.pprint(last_black_blocks)



n = int(input()) # 8 x 8의 미로
graph = [list(map(int,input().strip())) for _ in range(n)]
path_costs = [[0]*n for _ in range(n)]
directions = [(-1,0),(1,0),(0,1),(0,-1)]
# print(graph, path_costs)
dijk(1234)

# for _ in range(m):
#     src, dst, cost = map(int,input().split())
#     graph[src].append((cost,dst))
#     # graph[dst].append((cost,src)) # 양방향일 경우

# start_n = int(input())
# end_n = int(input())
