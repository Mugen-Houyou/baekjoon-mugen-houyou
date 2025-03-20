# 영역의 개수: 네방향, 범위내, 미방문
# 이 문제에서는 "특정 높이 이상" 조건이 더해짐.

from collections import deque
import sys
input = sys.stdin.readline

def bfs(v, row, col):
    global dq
    global result
    print(f'CURR R,C: {row}, {col}, {board[row][col]}')
    print("CURR DQ:",str(dq))
    print("RESULT:",result)

    # (탐색 중단 조건) 벽이거나 물높이보다 낮으면, 
    if (row<0 or col<0) or (row>=n-1 or col>=n-1) or board[row][col]<=v : 
        # dq가 비어있는지 체크, 뭐가 있으면 리셋 후 리턴 +=1, 비어있으면 그냥 리턴, 
        if len(dq) >= 1:
            result += 1
            dq = deque()
            return
        else:
            return
    # (탐색 지속 조건)
    else:
        # 해당되면 dq에 밀어넣음
        print("appended:",row,col)
        board[row][col]=99999999
        dq.append((row,col))

    # 탐색 - 상, 하, 좌, 우
    for k,l in [(-1,0),(1,0),(0,-1),(0,1)]:
        bfs(v,row+k,col+l)

n = int(input())
board = [None]*n
result = 0 
dq = deque()

# 입력
for i in range(n):
    board[i] = list(map(int,input().split()))

for v in range(1,101):
    for row in range(n):
        for col in range(n):
            bfs(v,row,col)

print(result)