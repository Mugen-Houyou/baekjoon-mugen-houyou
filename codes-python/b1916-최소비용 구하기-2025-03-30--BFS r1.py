import heapq
import math
import sys

"""
백준 1916 "최소비용 구하기"
문제:
N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.
입력:
첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.
그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.
출력:
첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.
예제 입력 1:
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5

예제 출력 1:
4
"""
def dijk():
    global n,m,graph,start_n,end_n

    hq = [(0,start_n)]
    dists = [math.inf for _ in range(len(graph))]
    dists[start_n] = 0

    while hq:
        acc_cost, curr = heapq.heappop(hq)

        if dists[curr] < acc_cost: 
            continue

        for c, nei in graph[curr]:
            if dists[nei] <= acc_cost+c:
                continue
            dists[nei] = acc_cost+c
            heapq.heappush(hq, (dists[nei], nei))

    return dists[end_n]


# 입력 & 세팅
input_str = sys.stdin.read().split()
idx = 0

n = int(input_str[idx]); idx+=1  # 노드 수
m = int(input_str[idx]); idx+=1  # 에지 수
graph = [[] for _ in range(n+1)]

for i in range(m):
    src = int(input_str[idx])
    dst = int(input_str[idx+1])
    cost = int(input_str[idx+2])
    idx += 3
    graph[src].append((cost,dst))

start_n = int(input_str[idx])
end_n = int(input_str[idx+1])

# 계산 & 출력
sys.stdout.write(f"{dijk()}\n")
