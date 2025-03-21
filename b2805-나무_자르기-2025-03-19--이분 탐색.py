import math

count, target_num = map(int,input().split())
trees = list(map(int,input().split()) )

low, high = 0, max(trees)

while low <= high:
    mid = (low + high) // 2  # 상한값 찾으려면 내림 (math.floor()와 같음)
    sum_cut = sum((trees[i] - mid) for i in range(len(trees)) if trees[i] > mid)
    # print(f'LOOP START POINT: sum_cut {sum_cut} < target_num {target_num}, low, mid, high {low, mid, high}')
    
    if sum_cut >= target_num: 
        # print(f'sum_cut {sum_cut} >= target_num {target_num}, low, mid, high {low, mid, high}')
        result = mid
        low = mid + 1 # 더 많다 ==> low를 갱신! mid보다 1 높여라.
    else:
        # print(f'sum_cut {sum_cut} < target_num {target_num}, low, mid, high {low, mid, high}')
        high = mid - 1 # 모자라다 ==> high를 mid보다 1 높여라.
    
    asdf = f'LOOP END POINT: sum_cut {sum_cut} < target_num {target_num}, low, mid, high {low, mid, high}'
    # input(asdf)

print(result)
