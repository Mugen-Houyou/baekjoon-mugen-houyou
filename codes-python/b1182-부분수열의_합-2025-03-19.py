import itertools

case_count, target = map(int,input().split())
numbers = list(map(int,input().split()))
result = 0

for i in range(1,case_count+1):
    comb = itertools.combinations(numbers,i)
    for c in comb:
        if sum(c) == target:
            result += 1
            
print(result)