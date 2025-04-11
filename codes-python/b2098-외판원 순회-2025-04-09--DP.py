import sys
import heapq
INF = 1<<59

def lowest_cost():
    start_n = 0
    hq = [(0,start_n)] # (비용, 도시)
    dist = [INF]*len(matrix)
    dist[start_n] = 0

    while hq:
        acc_cost, curr_n = heapq.heappop(hq)

        if visiteds[curr_n]:
            continue
        visiteds[curr_n] = True

        for nei, cost in enumerate(matrix[curr_n]):
            if cost!=0 and dist[nei] > acc_cost+cost: #not visiteds[nei]:
                dist[nei] = acc_cost+cost
                heapq.heappush(hq, (dist[nei], nei))

    print(dist)


input_str = sys.stdin.read().strip().split("\n")
N = int(input_str[0]) # 도시 수 N
matrix = [list(map(int,asdf.split())) for asdf in input_str[1:]]
visiteds = [False for _ in range(N)]
result = 0 # 비용

lowest_cost()