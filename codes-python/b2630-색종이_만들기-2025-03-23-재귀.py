import sys
input = sys.stdin.readline

size = int(input())
board = [list(map(int,input().split())) for _ in range(size)]
result = [0,0]

def check_uniform(start_row,start_col,end_row,end_col):
    start_val = board[start_row][start_col]

    for r in range(start_row,end_row+1):
        for c in range(start_col,end_col+1):
            if  board[r][c] != start_val: return -1

    result[start_val] += 1 
    return 0

def count_paper(paper_size:int,start_row,start_col,end_row,end_col) -> int:
    if check_uniform(start_row,start_col,end_row,end_col) == 0: return
    else: 
        coord_forward = paper_size//2
        count_paper(coord_forward, start_row, start_col, start_row+coord_forward-1, start_col+coord_forward-1)
        count_paper(coord_forward, start_row, start_col+coord_forward, start_row+coord_forward-1, end_col)
        count_paper(coord_forward, start_row+coord_forward, start_col, end_row, start_col+coord_forward-1)
        count_paper(coord_forward, start_row+coord_forward, start_col+coord_forward, end_row, end_col)

count_paper(size,0,0,size-1,size-1)
print(*result , sep="\n")
