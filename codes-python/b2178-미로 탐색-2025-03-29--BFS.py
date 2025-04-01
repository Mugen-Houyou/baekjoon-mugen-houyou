# 迷路探索
from collections import deque
import sys
input=sys.stdin.readline

def is_within_bounds(row, col):
    global rows_n, cols_n
    return (0<=row<rows_n) and (0<=col<cols_n)

def bfs_maze(sr, sc, er, ec): # 시작 row, 시작 col, 끝 row, 끝 col
    global maze, rows_n, cols_n

    dq = deque()
    path_costs = [[0]*cols_n for _ in range(rows_n)]
    dq.append((sr,sc))
    path_costs[sr][sc] = 1

    while dq:
        cr, cc = dq.popleft()
        if cr==er and cc==ec: 
            return path_costs[er][ec]

        # 4방향, 범위내, 조건 맞는가? ==> dq에 삽입.
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = cr+dr, cc+dc
            if (is_within_bounds(nr, nc)
                and maze[nr][nc]=="1"
                and path_costs[nr][nc]==0
            ):
                dq.append((nr, nc))
                path_costs[nr][nc] = path_costs[cr][cc]+1


rows_n, cols_n = map(int,input().split()) # N, M
maze = [input().strip() for _ in range(rows_n)]

print(bfs_maze(0,0,rows_n-1,cols_n-1))
