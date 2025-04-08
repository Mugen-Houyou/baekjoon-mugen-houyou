import sys
input=sys.stdin.readline

# 냅색 문제:

# 1. 베이스 케이스 설정
# 2. dp[물건의 인덱스][가방의 무게] = 해당 경우의 최대의 가치
#   예시: dp[1][0] = 1번 물건까지 고려 && 가방 무게 10까지 고려했을 때 얻을 수 있는 최대의 가치
# 3. 점화식은 아래와 같음
#   1) 현재 물건을 안 고르는 경우: 위칸꺼 그대로 가져옴 (=dp[i-1][w])
#   2) 현재 물건을 고르는 경우(w >= W[i]): max(dp[i-1][w], dp[i-1][w-W[i]] + 현재 물건의 가치)

# 즉, 정리하면,
# if w >= W[i]: dp[i][w] = max(dp[i=1][w], dp[i-1][w-W[i]] + V[i])
# else        : dp[i][w] = dp[i-1][w]

def knapsack():
    global N, K, stuffs, dp

    for i in range(1, N+1):
        stuff_w, stuff_v = stuffs[i-1] # 지금 이 물건의 무게 & 가치
        for knsk_w in range(K+1):        # 각 무게 한도에 대해
            if knsk_w >= stuff_w:          # 지금 이 물건을 담을 수 있는 경우
                dp[i][knsk_w] = max(dp[i-1][knsk_w], dp[i-1][knsk_w-stuff_w] + stuff_v)
            else:                          # 지금 이 물건을 못 담는 경우
                dp[i][knsk_w] = dp[i-1][knsk_w]

    return dp[N][K]


N,K = map(int,input().split()) # 물품 수 N, 최대 무게 K
stuffs = [list(map(int,input().split())) for _ in range(N)] # (물건무게, 물건가치)의 리스트. 위 W와 V를 합친 형태.
dp = [[0]*(K+1) for _ in range(N+1)]
print(knapsack())
