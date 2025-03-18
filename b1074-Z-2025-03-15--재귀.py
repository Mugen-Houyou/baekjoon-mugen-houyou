'''
한수는 크기가 2^N × 2^N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.

N > 1인 경우, 배열을 크기가 2^(N-1) × 2^(N-1)로 4등분 한 후에 재귀적으로 순서대로 방문한다.

N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.
'''
def z(n,row,column):
    if n == 0:
        return 0
    half = (2**n) // 2 # 2^(n-1) since n은 단순히 크기가 아니라 2^N의 n.
    # 2^(n-1) x 2^(n-1)로 나누기
    if row < half and column < half: # 1사분면
        return z(n-1,row,column)
    elif row < half and column >= half: # 2사분면
        return (half**2) + z(n-1,row,column-half)
    elif row >= half and column < half: # 3사분면
        return (half**2)*2 + z(n-1,row-half,column)
    else: # 4사분면
        return (half**2)*3 + z(n-1,row-half,column-half)

n,r,c = map(int, input().split())    

print(z(n, r, c))