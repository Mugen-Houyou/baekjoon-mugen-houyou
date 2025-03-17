# 참고: 다이나믹 프로그래밍을 사용하지 않은 코드입니다.

import itertools
import sys
input = sys.stdin.readline

# 입력 및 세팅
n_count = int(input())
tmp_perms = [i+1 for i in range(n_count-1)]

costs = [None]*n_count # 문제에서 입력받은 비용
for i in range(n_count):
    costs[i] = list(map(int,input().split()))
# 입력 및 세팅 끝

# 탐색
perm_list = list(itertools.permutations(tmp_perms)) # 전체 경로 순열 (앞뒤제외!)
perm_list_cost = [None]*len(perm_list)

# 전체 경로 비용 측정
for i in range(len(perm_list_cost)):
    tmp_list = [0, *perm_list[i], 0]
    print(tmp_list)
    cost_sum = 0
    for j in range(n_count): 
        # 0123 => 0,1/1,2/2,3/3,0 
        # 갈 수 없는 길은 거르기
        if costs[tmp_list[j]][tmp_list[j+1]]==0:
            cost_sum == 99999999
        # 되면 ㄱㄱ
        else:
            cost_sum += costs[tmp_list[j]][tmp_list[j+1]]
    perm_list_cost[i] = cost_sum

# 측정된 비용 토대로 최저값 계산
for i in range(len(perm_list)):
    print(perm_list[i],":",perm_list_cost[i])

print(min(perm_list_cost))