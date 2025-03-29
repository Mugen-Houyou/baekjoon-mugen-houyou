# 迷路探索
from collections import deque
import sys
input=sys.stdin.readline

def is_beyond_wall(row, col):
    global rows_count, cols_count

    if not (0<=row<rows_count and 0<=col<cols_count):
        return True
    
    return False

def bfs(start_row, start_col, end_row, end_col):
    global rows_count, cols_count, maze

    dq = deque()
    path_costs = [[0]*cols_count for _ in range(rows_count)]
    dq.append((start_row,start_col))
    path_costs[start_row][start_col] = 1    

    while dq:
        curr_row, curr_col = dq.popleft()
        if curr_row==end_row and curr_col==end_col: 
            return path_costs[end_row][end_col]

        # 4방향, 범위내, 조건 맞는가? ==> dq에 삽입.
        for row_ahead, col_ahead in [(-1,0),(1,0),(0,-1),(0,1)]:
            next_row, next_col = curr_row+row_ahead, curr_col+col_ahead
            if (not is_beyond_wall(next_row, next_col)
                and maze[next_row][next_col]=="1"
                and path_costs[next_row][next_col]==0
            ):
                dq.append((next_row, next_col))
                path_costs[next_row][next_col] = path_costs[curr_row][curr_col]+1


rows_count, cols_count = map(int,input().split()) # N, M
maze = [input().strip() for _ in range(rows_count)]

print(bfs(0,0,rows_count-1,cols_count-1))
