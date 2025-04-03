import sys
input=sys.stdin.readline
ABOUT_MAX = 1<<30 
ABOUT_MIN = -1<<30

def dfs_rcsv(idx, curr, pl, su, mu, di):
    global max_val, min_val

    if idx == n:
        max_val = max(curr, max_val)
        min_val = min(curr, min_val)
        return

    if pl > 0:
        dfs_rcsv(idx+1, curr + numbers[idx], pl-1, su, mu, di)
    if su > 0:
        dfs_rcsv(idx+1, curr - numbers[idx], pl, su-1, mu, di)
    if mu > 0:
        dfs_rcsv(idx+1, curr * numbers[idx], pl, su, mu-1, di)
    if di > 0:
        if curr < 0: # 중간결과값이 음수일 경우 별도 대응 필요
            dfs_rcsv(idx + 1, -(-curr // numbers[idx]), pl, su, mu, di-1)
        else:
            dfs_rcsv(idx + 1, curr // numbers[idx], pl, su, mu, di-1)
    """ "C++14 기준"이란
    => (음수/양수) 시 결과가 0에 가까운 방향(즉, 0으로 'truncate'하는 방식)으로 처리.

    예: C++14 -7 / 3 = -2 (단순히 소수점 이하를 버리는 방식) vs. 파이썬 -7 // 3 = -3 ("바닥 나눗셈" - 음수 결과의 경우 소수점 아래를 내림하여 더 작은 정수로)
    """


# 입력 & 세팅
n = int(input()) # 수의 개수 n
numbers = list(map(int,input().split())) # 수열 A
operations = list(map(int,input().split())) # 개수 of 덧, 뺄, 곱, 나 
max_val = ABOUT_MIN
min_val = ABOUT_MAX

# 계산
dfs_rcsv(1, numbers[0], operations[0], operations[1], operations[2], operations[3])

# 출력
print(max_val)
print(min_val)