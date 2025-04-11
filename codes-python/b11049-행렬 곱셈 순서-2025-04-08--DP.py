import sys
INF = 1<<59

def dp_matmul():
    for chain_len in range(2, N+1): # 체인 길이는 2부터 시작!!
        for i in range(0, N-chain_len+1):
            j = i+chain_len-1 # 마지막 행렬 인덱스. 즉, 행렬 범위 [i,j]를 곱한다면, i는 시작이고, j = i+chain_len-1이 마지막.
            dp[i][j] = min(dp[i][k] + dp[k+1][j] + rowcol[i][0]*rowcol[k][1]*rowcol[j][1] 
                           for k in range(i,j))
    return


# 입력 & 세팅
input_str = sys.stdin.read().strip().split("\n")
N = int(input_str[0])
rowcol = [list(map(int, asdfasdf.split())) for asdfasdf in input_str[1:]]
dp = [[0]*N for _ in range(N)]

# 처리 & 출력
dp_matmul()
print(dp[0][-1])


# dp_matmul()의 for문은 아래와 같이 개선 가능
# 
#     for chain_len in range(2, N+1):
#         for i in range(0, N-chain_len+1):
#             j = i+chain_len-1 
#             best = INF
#             for k in range(i, j):
#                 cost = dp[i][k] + dp[k+1][j] + rowcol[i][0]*rowcol[k][1]*rowcol[j][1]
#                 if cost < best:
#                     best = cost
#             dp[i][j] = best
