import sys
from collections import defaultdict

input = sys.stdin.readline

def dfs_bipt(start, graph, colors):
    stack = [start]
    colors[start] = 1

    while stack:
        node = stack.pop()
        for nei in graph[node]:
            if colors[nei] == 0:
                colors[nei] = -colors[node]
                stack.append(nei)
            elif colors[nei] == colors[node]:
                return False
    return True

def is_bipt(graph, nodes_n):
    colors = [0] * (nodes_n + 1)
    for node in range(1, nodes_n + 1):
        if colors[node] == 0:
            if not dfs_bipt(node, graph, colors):
                return False
    return True


# 입력 & 세팅
input_data = sys.stdin.read().split()
idx = 0
test_cases_n = int(input_data[idx])
idx += 1

output = []
# 계산
for _ in range(test_cases_n):
    nodes_n = int(input_data[idx])
    edges_n = int(input_data[idx + 1])
    idx += 2

    graph = defaultdict(list)
    for _ in range(edges_n):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        idx += 2
        graph[a].append(b)
        graph[b].append(a)

    # 출력 중간 저장
    output.append("YES" if is_bipt(graph, nodes_n) else "NO")

# 출력
print("\n".join(output))
