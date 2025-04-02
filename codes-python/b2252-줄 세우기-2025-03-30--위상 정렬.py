import sys
from collections import deque
input=sys.stdin.readline

def tp_sort():
    global comparisons, indegrees
    dq = deque([node for node,val in enumerate(indegrees) if val==0])
    result = []

    while dq:
        node = dq.popleft()
        result.append(node) 
                                        # 만약 현재 노드 A를 탐색 중이며,
        for nei in comparisons[node]:   # A => B, A => C, ...면,
            indegrees[nei] -= 1         # A의 인접 노드들 싹 다 검색
            if indegrees[nei] == 0:     # 그들의 차수를 1씩 깎음
                dq.append(nei)          # 그리고 그들 중 차수 0이 다음 차례

    return result[1:] # 0이 무조건 나오므로


# 입력 & 세팅
n,m = map(int,input().split())          # 학생 수 n, 비교 횟수 m
comparisons = [[] for _ in range(n+1)]
indegrees = [0]*(n+1)                   # 해당 노드에게 들어오는 엣지 수

for _ in range(m):
    src,dst = map(int,input().split())
    comparisons[src].append(dst)            # A => B 노드면, 
    indegrees[dst] += 1                   # B의 indegree를 1 높임.

# 계산 & 출력
print(*tp_sort())
