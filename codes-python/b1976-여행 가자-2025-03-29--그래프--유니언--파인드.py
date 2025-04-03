import sys
input = sys.stdin.readline

def find(i):
    if parents[i] != i:
        parents[i] = find(parents[i])  # 경로 압축
    return parents[i]

def union(i, j):
    root_i = find(i)
    root_j = find(j)
    
    if root_i == root_j:
        return  # 이미 같은 집합이면 합치지 않음

    parents[root_i] = root_j

    # # Optional: rank가 낮은 트리를 rank가 높은 트리 밑에 붙임
    # if ranks[root_i] < ranks[root_j]:
    #     parents[root_i] = root_j
    # elif ranks[root_i] > ranks[root_j]:
    #     parents[root_j] = root_i
    # else:
    #     parents[root_j] = root_i
    #     ranks[root_i] += 1  # 높이가 같으면 하나의 트리 높이를 1 증가시킴


# 입력 & 세팅
cities_count = int(input())
planned_c_count = int(input())

cities = [[] for _ in range(cities_count+1)]
for i in range(1,cities_count+1):
    cities[i] = [0] + list(map(int, input().split()))
plans = list(map(int, input().split()))

parents = [i for i in range(cities_count + 1)] # union-find를 위한 부모
# ranks = [0] * (cities_count + 1) # Optional: union-by-rank 기법을 위한 랭크
# 높이가 더 낮은 트리를, 더 높은 트리 밑에 붙이는 것이 랭크임
# union by rank + path compression 조합 => 평균 시간복잡도가 거의 상수에 가까움: O(α(N))

# 직접 연결된 도시들을 union 연산을 통해 동일 집합으로 합침으로써, 
# 도시들의 연결 상태를 관리 가능
for i in range(1, cities_count + 1): 
    for j in range(1, cities_count + 1):
        if cities[i][j] == 1:
            union(i, j)

# Find 연산을 통해
# 여행 계획상 도시들이 같은 집합에 속하는지 확인 가능
result = True
for i in range(1, len(plans)): 
    if find(plans[0]) != find(plans[i]): 
        result = False
        break

print('YES' if result else 'NO')
