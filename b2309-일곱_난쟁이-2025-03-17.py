# 알고리즘을 직접 구현

# import sys
# input=sys.stdin.readline

nanj = [int(input()) for _ in range(9)]

for i in range(len(nanj)):
    for j in range(len(nanj)):
        if i==j: continue
        result_cands = [nanj[k] for k in range(len(nanj)) if k!=i and k!=j]
        if sum(result_cands) == 100:
            for result_nanj in sorted(result_cands):
                print(result_nanj)
            exit()
        