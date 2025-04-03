# 굴로 이동하기 위한 최소 시간을 구하는 프로그램을 작성.
import sys
from collections import deque
input=sys.stdin.readline

def is_within_bounds(curr_x,curr_y):
    global r,c
    return (0<=curr_x<r) and (0<=curr_y<c)

def bfs_water_progression(): # 참고: 한 단계씩만 전진함.
    global r,c,graph
    
    proceedables = [(x,y) 
                    for x,row in enumerate(graph) 
                    for y,col in enumerate(row) 
                    if col == "*"]

    for cr,cc in proceedables:
        for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
            newr, newc = cr+dr, cc+dc
            if is_within_bounds(newr,newc) and graph[newr][newc] == ".":
                graph[newr][newc] = "*"
    return

def bfs():
    global r,c,graph,visiteds,directions,st_row,st_col

    time = 0
    dq = deque([(st_row, st_col)])
    visiteds[st_row][st_col] = True
    result_loc = (st_row,st_col)

    while dq:
        bfs_water_progression() # 물 한 번 확산
        
        # 이번 시간의 고슴도치 움직임
        for _ in range(len(dq)): # 참고 - for문이 실행되기 전에 dq의 길이가 결정되고, 그 길이만큼 반복하게 됨. 즉, 아무리 dq에 새로운 것들이 append되어도 for문은 최초 len(dq)만큼만 반복함. 레벨 단위 탐색 기법.
            x, y = dq.popleft()
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if is_within_bounds(nx, ny):
                    # 다음이 도착지 ==> 시간+1 리턴하고 끝
                    if graph[nx][ny] == 'D':
                        return time + 1
                    # 다음이 빈칸 && 미방문 ==> 큐에 추가
                    if graph[nx][ny] == '.' and not visiteds[nx][ny]:
                        visiteds[nx][ny] = True
                        dq.append((nx, ny))

        time += 1
    return "KAKTUS" 


r,c = map(int,input().split()) # r행 c열짜리 맵, 즉 c x r 사이즈의 맵.
graph = sys.stdin.read().split("\n") # 남은 거 다 읽기
graph = list(map(list,graph))
print(graph)
visiteds = [[False]*(c) for _ in range(r)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
st_row, st_col = next((x, y) 
                      for x, row in enumerate(graph) 
                      for y, col in enumerate(row) 
                      if col == "S")
ed_row, ed_col = next((x, y) 
                      for x, row in enumerate(graph) 
                      for y, col in enumerate(row) 
                      if col == "D")

print(bfs())
