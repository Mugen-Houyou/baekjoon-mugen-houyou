import sys
input=sys.stdin.read

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x]) # 경로 압축 적용
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_b] = root_a

# 입력 & 세팅
input_str = sys.stdin.read().rstrip().split("\n")
n, m = map(int, input_str[0].split())
graph = input_str[1:]
parent = [i for i in range(n+1)] # 부모 초기화

# 처리 & 출력
for i in range(len(graph)):
    op, a, b = map(int, graph[i].split()) # 0,a,b => a가 포함된 집합과 b가 포함된 집합을 합침 / 1,a,b => a, b가 같은 집합에 포함되어 있는지를 확인
    if op == 0: 
        union(a, b)
    elif op == 1:
        print("YES" if find(a) == find(b) else "NO") # 동일 루트인지 확인하여 출력