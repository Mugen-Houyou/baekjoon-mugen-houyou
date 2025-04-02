import sys
input=sys.stdin.readline

"""
문제:
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
예제 입력 1:
7
1 6
6 3
3 5
4 1
2 4
4 7
예제 출력 1:
4
6
1
3
1
4
예제 입력 2:
12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
예제 출력 2:
1
1
2
3
3
4
4
5
5
6
6
"""

def dfs(root: int):
    global graph, parents
    
    stk = [root] # 루트 노드부터 시작
    parents[root] = 0
    tmp_parent = 0

    while stk:
        node = stk.pop()
        tmp_parent = node
        for nei in graph[node]:
            if parents[nei] != -1: continue # 부모 이미 등록돼 있으면 생략
            parents[nei] = tmp_parent
            stk.append(nei)


nodes_count = int(input())
graph = {x: [] for x in range(nodes_count+1)}
# visiteds = [False]*(nodes_count+1)
parents = [-1 for _ in range(len(graph))] # result에는 각 노드의 부모를 append할 것. 0, 1은 아무 의미 없으니 -1로 기본 설정.

for i in range(1,nodes_count):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(*parents[2:], sep="\n")