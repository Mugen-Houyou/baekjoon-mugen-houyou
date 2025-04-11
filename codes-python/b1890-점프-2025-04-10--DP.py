import sys
INF = 1<<63

def dp_solve():
    dp[1][1] = 1 # 시작점

    for i in range(1, N+1):
        for j in range(1, N+1):
            curr_of = matrix[i-1][j-1] 

            # if i==1 and j==1: # 시작점
            #     continue
            if curr_of == 0: # 진행불가칸
                continue

            if i+curr_of <= N:
                dp[i+curr_of][j] += dp[i][j]
            if j+curr_of <= N:
                dp[i][j+curr_of] += dp[i][j]

    return dp[-1][-1]

# 입력 & 세팅
input_str = sys.stdin.read().strip().split("\n")
N = int(input_str[0])
matrix = [list(map(int,asdf.split())) for asdf in input_str[1:]] # 각 칸에 적혀있는 수 = 현재 칸에서 갈 수 있는 거리
dp = [[0]*(N+1) for _ in range(N+1)]

# 처리 & 출력
print(dp_solve())
