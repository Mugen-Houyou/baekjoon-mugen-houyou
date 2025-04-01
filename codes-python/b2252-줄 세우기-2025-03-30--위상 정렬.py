import sys
from collections import deque
input=sys.stdin.readline

def tp_sort():
    global n,m,comparisons
    dq = deque()
    for i in range(n):
        
        pass


    return


n,m = map(int,input().split())
#comparisons = [list(map(int,input().split())) for _ in range(m)]
comparisons = [[] for _ in range(n+1)]
degree = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    comparisons[a].append(b)
    degree[b] += 1


