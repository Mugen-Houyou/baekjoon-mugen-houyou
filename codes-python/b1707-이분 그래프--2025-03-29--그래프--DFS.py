import sys
input = sys.stdin.readline

# Bipartite graph가 맞을 경우 True
# Bipartite graph가 아닐 경우 False
def dfs_bipt(root:int):
    global graph, colors
    stk=[root]
    colors[root] = 1

    while stk:
        node = stk.pop()

        for nei in graph[node]:
            if colors[nei] == 0: 
                colors[nei] = -colors[node]
                stk.append(nei)
            elif colors[node]==colors[nei]: 
                return False
    return True


def is_bipt():
    global graph, colors, nodes_n

    for node in range(1, nodes_n + 1):
        if colors[node] == 0:
            if not dfs_bipt(node):
                return False
    return True


# 입력 & 세팅
test_cases_n = int(input())
for _ in range(test_cases_n):
    nodes_n, edges_n = map(int,input().split())
    graph = { x:[] for x in range(1,nodes_n+1) }
    colors = [0]*(nodes_n+1)
    for i in range(edges_n):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # 계산 & 출력
    print('YES' if is_bipt() else 'NO')
