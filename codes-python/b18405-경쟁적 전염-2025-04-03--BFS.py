import sys
from collections import deque
input=sys.stdin.readline

def is_within_bounds(curr_x,curr_y):
    global n
    return (0<=curr_x<n) and (0<=curr_y<n)

def bfs_vir_progression(): # 참고: 한 단계씩만 전진하도록.
    global n,graph

    dq = deque()
    
    proceedables = [(x,y) 
                    for x,row in enumerate(graph) 
                    for y,col in enumerate(row) 
                    if col in range(1,k+1)]
    
    dq = deque(proceedables)

    for _ in range(len(proceedables)):
        cr,cc = dq.popleft()
        for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
            newr, newc = cr+dr, cc+dc
            if is_within_bounds(newr,newc) and graph[newr][newc] == "0":
                graph[newr][newc] = graph[cr][cc]

    return


n,k  = map(int,input().split()) # 
graph = [list(map(int,input().split())) for _ in range(n)]
s,x,y = map(int,input().split())
visiteds = [[False]*(n) for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

print(bfs_vir_progression())
