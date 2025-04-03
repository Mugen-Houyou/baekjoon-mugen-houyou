import sys
from collections import deque
input=sys.stdin.readline

def is_within_bounds(floor:int, row:int, col:int):
    global m,n,h
    return (0<=floor<h) and (0<=row<n) and (0<=col<m) 

def bfs_tomato():
    global m,n,h,block
    
    proceedables = [(f,r,c,0) 
                    for f in range(len(block)) 
                    for r in range(len(block[f])) 
                    for c in range(len(block[f][r])) 
                    if block[f][r][c] == 1]
    
    dq = deque(proceedables)
    days = 0 # 경과 일수 저장하려고
    
    while dq:
        f, r, c, day = dq.popleft()
        days = max(days, day)
        
        for df, dr, dc in ((1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)):
            nf, nr, nc = f+df, r+dr, c+dc
            if is_within_bounds(nf, nr, nc) and block[nf][nr][nc] == 0: # 이 조건에서 -1랑 1은 알아서 걸러짐
                block[nf][nr][nc] = 1
                dq.append((nf, nr, nc, 1+day))
    
    return (-1 if any(0 in col
                        for row in block
                        for col in row) else days)


# 입력 & 세팅
m,n,h = map(int,input().split()) # 가로 m, 세로 n, 높이 h
block = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]  # block[층][행][열]

# 계산 & 출력
print(bfs_tomato())
