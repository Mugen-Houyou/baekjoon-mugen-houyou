from collections import deque
import sys
input=sys.stdin.readline

def is_within_bounds(row, col):
    global rows_n, cols_n

    return (0<=row<rows_n) and (0<=col<cols_n)

def kazari():
    global rows_n,cols_n,visited,yuka,count

    for i in range(rows_n):
        for j in range(cols_n):
            if yuka[i][j] == '-':
                if j == 0 or yuka[i][j-1] != '-':
                    count += 1
            elif yuka[i][j] == '|':
                if i == 0 or yuka[i-1][j] != '|':
                    count += 1


# 입력 & 세팅
rows_n, cols_n = map(int,input().split()) # N, M
yuka = [input().strip() for _ in range(rows_n)]
count = 0

# 계산 & 출력
kazari()
print(count)
