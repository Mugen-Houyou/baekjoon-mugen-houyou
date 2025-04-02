import sys
from collections import deque
from collections import defaultdict
input=sys.stdin.readline

def tp_srt():
    global graph, default_sets, needs, indegrees  
    
    # 진입차수가 0인 노드를 모두 찾되, 0번 인덱스는 사용하지 않으므로 [1:]로 슬라이싱 (기본 부품들)
    dq = deque([node for node, val in enumerate(indegrees) if val == 0][1:])

    while dq:  
        dst = dq.popleft() 

        for nei, c in graph[dst]:

            # 만약 needs[dst]의 모든 요소가 0이라면, dst는 아직 어떤 기본 부품으로 분해되지 않았으므로
            # 이는 dst가 기본 부품임을 의미 (needs[dst]의 길이가 n+1이므로 모두 0이면 count(0)==n+1)
            if needs[dst].count(0) == n+1:
                # 부품 nei를 만들 때, 기본 부품 dst가 c개 필요하므로 해당 수량을 누적
                needs[nei][dst] += c
            else:
                # 만약 dst가 중간 부품이라면, 이미 기본 부품으로 분해된 정보(needs[dst])가 있음.
                # 이를 활용해 부품 nei를 만드는데 필요한 기본 부품 수를 갱신
                for i in range(1, n+1):
                    # 부품 dst를 c개 만들기 위해 필요한 i번 기본 부품의 개수는 (c*needs[dst][i])
                    needs[nei][i] += c*needs[dst][i]
            
            indegrees[nei] -= 1  # 부품 nei에 대해, dst의 처리가 완료되었으므로 진입차수를 1 감소

            if indegrees[nei] == 0:
                dq.append(nei)  # 모든 선행 부품이 처리되어 indegree가 0이 된 경우, dq에 추가해 이후 처리할 수 있도록 함
    return


n = int(input())
m = int(input())
graph = defaultdict(list)
default_sets = set()
needs = [[0]*(n+1) for _ in range(n+1)]
indegrees = [0 for _ in range(n+1)]

for _ in range(m):
    dst, src, cost = map(int,input().split())
    # set 관련
    default_sets.add(dst)

    # graph 관련 - 역방향으로 삽입하는 유형
    graph[dst].append((src,cost))
    indegrees[src] += 1
tp_srt()
for i in range(1,len(needs)):
    if i in default_sets: continue
    print(i, needs[i][-1])