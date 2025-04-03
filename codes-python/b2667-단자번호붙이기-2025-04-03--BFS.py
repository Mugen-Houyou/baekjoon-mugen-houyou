import sys
from collections import deque
input=sys.stdin.readline

def is_within_bounds(row,col):
    return 0<=row<size and  0<=col<size

def bfs(row,col,idx):
    dq = deque()
    dq.append((row,col))
    visiteds[row][col] = True
    count = 1

    while dq: 
        cr,cc = dq.popleft()
        
        for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
            nr,nc = cr+dr, cc+dc
            # 방문 조건: 네 방향 && 범위 내 && 미방문
            if (is_within_bounds(nr,nc)
                and not visiteds[nr][nc]
                and graph[nr][nc]==1
            ):
                dq.append((nr,nc))
                visiteds[nr][nc] = True
                count += 1

    result[idx] += count

size = int(input())
graph = [list(map(int,input().rstrip())) for _ in range(size)]
visiteds = [[False]*size for _ in range(size)]
result = []

for row in range(size):
    for col in range(size):
        # 1 && 미방문에서만 ㄱ
        if graph[row][col] == 1 and not visiteds[row][col]:
            result.append(0)
            bfs(row, col, len(result)-1)

result_f = sorted([r for r in result if r!=0])
print(len(result_f), *result_f, sep="\n") 
