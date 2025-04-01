# 영역의 개수: 네방향, 범위내, 미방문
# 이 문제에서는 "특정 높이 이상" 조건이 더해짐.

from collections import deque
import sys
input = sys.stdin.readline

def bfs(height,row,col):
    dq = deque()
    dq.append((row,col))
    visiteds[row][col] = 1

    while dq: # dq에 뭐라도 있는 동안
        current_row,current_col = dq.popleft()
        
        # 상/하/좌/우 한번씩 방문
        for row_step, col_step in ((-1,0),(1,0),(0,-1),(0,1)):
            next_row = current_row+row_step
            next_col = current_col+col_step
            # 방문 조건: 네 방향 / 범위 내 / 미방문 / h보다 높음
            if (0<=next_row<size 
                and 0<=next_col<size
                and visiteds[next_row][next_col]==0 
                and input_arr[next_row][next_col] > height
            ):
                dq.append((next_row,next_col))
                visiteds[next_row][next_col]=1

def solve(height):
    global size
    count = 0
    
    for row in range(size):
        for col in range(size):
            # 방문 조건: 범위 내 (생략) / 미방문 / h보다 높음
            if visiteds[row][col]==0 and input_arr[row][col]>height:
                bfs(height,row,col)
                count += 1

    return count


# 입력 & 세팅
size = int(input())
input_arr = [None]*size
result = 0 

for i in range(size):
    input_arr[i] = list(map(int,input().split()))

# 실행
for height in range(0,100):
    visiteds = [[0]*size for _ in range(size)] # 1이면 기방문, 0이면 미방문
    result = max(result,solve(height))

#출력
print(result)