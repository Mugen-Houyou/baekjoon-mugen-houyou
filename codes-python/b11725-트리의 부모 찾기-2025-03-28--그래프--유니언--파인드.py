import sys
input=sys.stdin.readline

# 딕셔너리 기반 그래프의 find 연산
def find(a):
    global parents
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parents[a] != a:
        return find(parents[a])
    return a

# 두 원소가 속한 집합을 합치기
def union(a, b):
    global parents
    # 각각의 원소가 속한 집합을 찾고, 더 작은 값을 부모로 설정
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

# 경로 압축 기법을 사용한 find 연산
def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]
        
# 두 원소가 속한 집합을 합치기 (경로 압축 기법 사용)
def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


nodes_count = int(input())
graph = {x: [] for x in range(nodes_count+1)}
parents = [i for i in range(nodes_count + 1)]

for i in range(1,nodes_count):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 모든 노드간 연결 상태에 대해 union_parent 연산 수행
for i in range(1, nodes_count+1):
    for j in graph[i]:
        union_parent(parents, i, j)

# 각 원소가 속한 집합을 알기 위해서는 반복문을 수행하여 parents 배열에 대해 find_parent(parent, i)를 출력한다.
# 이때, find_parent 함수는 경로 압축 기법을 사용하여 부모 노드를 찾는다.
for i in range(1, nodes_count + 1):
    find_parent(parents, i)

# 각 노드들에 대한 부모 노드 출력
print(parents)
