import sys
from itertools import permutations

input=sys.stdin.readline

# 시작점 추가 - route를 넣으면, route[0]으로 갈 수 있는 노드들을 찾아, 해당 노드들의 리스트를 result로 리턴함
def seek_starting_point(route:list):
    result = [] 
    return result

# 끝점 추가 - route를 넣으면, route[-1]에서 갈 수 있는 노드들을 찾아, 해당 노드들의 리스트를 result로 리턴함
def seek_ending_point(route:list):
    result = [] 
    return result




# 시작점과 끝점을 제외하고, 산책 경로 위에 실내 장소가 있으면 안됩니다.
def dfs(root:int, max_len:int): # max_len은 최대 거리
    global nio,graph,visiteds

    stk = [root]
    result = []

    while stk:
        node = stk.pop()
        if visiteds[node]: continue
        visiteds[node] = True
        result.append(node)

        # 더 이상 자식이 없으면, 실외 여부 확인, 이후 종료
        if len(graph[node])==0:
            if nio[node]==0:
                

        for nei in sorted(graph[node],reverse=True):
            if visiteds[nei]: continue
            stk.append(nei)


    return 


n = int(input()) # 노드 수
nio = "."+input() # 실내 1, 실외 0
indoors = [node for node in range(n+1) if nio[node]=="1"]
outdoors = [node for node in range(n+1) if nio[node]=="0"]
graph = [[] for _ in range(n+1)]
visiteds = [False for _ in range(n+1)]

while True:
    try: a,b = map(int,input().split())
    except: break
    graph[a].append(b)
    graph[b].append(a)

for ml in range(2,n+1): # 2개부터 n개까지
    for start in indoors:
        visiteds = [False for _ in range(n+1)]
        print(dfs(start,ml))