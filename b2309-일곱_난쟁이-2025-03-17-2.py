# 내장 라이브러리를 사용

from itertools import combinations
# import sys
# input = sys.stdin.readline

nanjs = [int(input()) for _ in range(9)]
total = sum(nanjs)

for cand1, cand2 in combinations(nanjs, 2):
    if total - (cand1 + cand2) == 100:
        result = nanjs.copy()
        result.remove(cand1)
        result.remove(cand2)
        for num in sorted(result):
            print(num)
        exit()
