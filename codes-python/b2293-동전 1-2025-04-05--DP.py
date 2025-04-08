import sys
input = sys.stdin.readline

def dp_coin():
    global N,K,coin_types,dp

    for i in range(N+1):
        dp[i][0] = 1 # 베이스 케이스 - 도합 0원인 경우 1가지 (동전 아예 안 씀)

    for i in range(1, N+1):
        coin = coin_types[i-1]  # i번째 동전의 가치
        for val_total in range(1, K+1):
            if val_total >= coin: # 동전 i를 사용 가능 (도합인 val_total가 coin 이상)
                dp[i][val_total] = dp[i-1][val_total] + dp[i][val_total-coin]
            else: # 동전 i를 안 씀
                dp[i][val_total] = dp[i-1][val_total]
            # dp[i][val_total] = (dp[i-1][val_total] + dp[i][val_total-coin]) if val_total >= coin else dp[i-1][val_total]

    return dp[N][K]


# 입력 & 세팅
N, K = map(int, input().split())
coin_types = [int(input().strip()) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)] # dp[i][j]: 첫 번째부터 i번째 동전까지 사용해서 합이 j가 되는 경우의 수

# 계산 & 출력
print(dp_coin())
