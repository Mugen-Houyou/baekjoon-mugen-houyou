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

    # rank가 낮은 트리를 rank가 높은 트리 밑에 붙임
    if ranks[root_i] < ranks[root_j]:
        parents[root_i] = root_j
    elif ranks[root_i] > ranks[root_j]:
        parents[root_j] = root_i
    else:
        parents[root_j] = root_i
        ranks[root_i] += 1  # 높이가 같으면 하나의 트리 높이를 1 증가시킴


# 입력 & 세팅
cities_count = int(input())
parents = [i for i in range(cities_count + 1)]
ranks = [0] * (cities_count + 1)
planned_c_count = int(input())

cities = [[0] * (cities_count + 1)]
for _ in range(cities_count):
    cities.append([0] + list(map(int, input().split())))

plans = list(map(int, input().split()))

# 모든 도시 간 연결 상태에 대해 union 연산 수행
for i in range(1, cities_count + 1):
    for j in range(1, cities_count + 1):
        if cities[i][j] == 1:
            union(i, j)

# 여행 계획의 모든 도시가 같은 집합에 속하는지 확인
result = True
for i in range(1, len(plans)):
    if find(plans[0]) != find(plans[i]):
        result = False
        break

print('YES' if result else 'NO')
