import sys
input = sys.stdin.readline

def max_qual(): # maximum qualified applicants (최대 합격자수)
    result = 1
    best_intv = apps[0][1]

    for i in range(1, len(apps)):
        # unqualified = any(res>curr_res and intv>curr_intv for curr_res, curr_intv in apps) # naive approach
        qualified = apps[i][1] < best_intv
        if qualified:
            best_intv = apps[i][1]
            result += 1

    return result


# 입력 & 세팅
test_cases = int(input())
for _ in range(test_cases):
    N = int(input())
    apps = sorted([list(map(int,input().split())) for _ in range(N)]) # applicants라서 apps

    # 처리 & 출력
    print(max_qual())
