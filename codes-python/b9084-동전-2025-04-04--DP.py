import sys
sys.setrecursionlimit(1<<16)
input=sys.stdin.readline

def dp_coin(i, remaining):
    if remaining == 0: # 남은 금액이 0? 방법은 하나뿐.
        return 1
    if remaining < 0 or i >= N: # 남은 금액이 음수 or 동전이 더 없음? 그냥 없는 경우임.
        return 0
    
    if momoi[i][remaining] != -1: # 메모이제이션으로부터 반환
        return momoi[i][remaining]
    
    # 메모이제이션에 없는 경우
    # "현재 동전인 coins[i]를 사용할 경우 & 사용하지 않고 넘어갈 경우"의 합산
    momoi[i][remaining] = dp_coin(i, remaining-coin_types[i]) + dp_coin(i+1, remaining)
    return momoi[i][remaining]


# 입력 & 세팅
T = int(input()) # 테스트 케이스 수 N

for _ in range(T):
    N = int(input()) # 동전의 가짓수 N
    coin_types = list(map(int,input().split())) # 동전 종류   
    M = int(input()) # 금액 M
    momoi = [[-1] * (M + 1) for _ in range(N + 1)] # dp[i][r] : coins[i:] (i번 인덱스부터 사용하여) r원을 만드는 방법의 수

    # 처리 & 출력
    print(dp_coin(0, M))

