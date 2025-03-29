import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph: dict, stk: list):
    global marked
    if len(stk)==0: return
    
    popped = stk.pop()
    print(popped, end=" ")
    
    for cn in graph[popped]:
        if cn in marked: continue
        stk.append(cn)
        marked.add(cn)
        
    for i in range(len(graph[popped])):
        dfs(graph, stk)

        
def dfs_revised(graph: dict, node: int):
    global marked
    print(node, end=" ")

    for neighbor in sorted(graph[node]):
        if neighbor not in marked:
            marked.add(neighbor)
            dfs_revised(graph, neighbor)


def bfs(graph: dict, start_node: int):
    global marked
    queue = deque([start_node])

    while True:
        current = queue.popleft()
        print(current, end=" ")
        
        # for neighbor in graph[current]:
        for neighbor in sorted(graph[current]):
            if neighbor not in marked:
                marked.add(neighbor)
                queue.append(neighbor)

        if len(queue) == 0: break


nodes_count, edges_count, start_node = map(int, input().split())
graph = {i: [] for i in range(1, nodes_count + 1)} # 노드가 1,2,3,4,... 같은 식일 것이라고 가정

for _ in range(edges_count):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향으로 넣자.

# stk = [1]
marked = set([start_node])
dfs_revised(graph, start_node)
print()
marked = set([start_node])
bfs(graph, start_node)
