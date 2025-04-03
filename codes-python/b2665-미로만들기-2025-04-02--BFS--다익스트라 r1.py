# 검은 방에서 흰 방으로 바꾸어야 할 최소의 수를 구하는 프로그램을 작성.
import sys
from collections import deque
input = sys.stdin.readline

def is_within_bounds(row, col):
    global n
    return (0<=row<n) and (0<=col<n)

def bfs():
    global n, graph, path_costs, directions, start_n

    dq = deque()
    dq.append(start_n)
    path_costs[start_n[0]][start_n[1]] = 0 # 0으로.

    while dq:
        crow, ccol = dq.popleft()

        # 다음 움직임 시작
        for dr, dc in directions:
            nr, nc = dr+crow, dc+ccol

            if not is_within_bounds(nr,nc):
                continue

            # 검은 방이면 현재+1, 아니면 현재 그대로
            new_cost = (path_costs[crow][ccol]+1 if graph[nr][nc] == '0' else path_costs[crow][ccol])
        
            if path_costs[nr][nc] > new_cost: # 갱신 필요 경우
                path_costs[nr][nc] = new_cost
                dq.append((nr, nc))

    return


# 입력 & 세팅
n = int(input()) # 8 x 8의 미로
graph = [list(input().rstrip()) for _ in range(n)] # rstrip() ==> 뒤쪽 strip.
path_costs = [[1<<31]*n for _ in range(n)] # 여기까지 오기까지 벽돌을 몇 개 뚫었나?
directions = [(-1,0),(1,0),(0,1),(0,-1)]
start_n = (0,0) # 시작 행, 시작 열

# 계산 
bfs()

# 출력
print(path_costs[-1][-1])
