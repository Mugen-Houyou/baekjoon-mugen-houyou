import sys
input = sys.stdin.readline

test_case_count = int(input())
stk = []
result = 0

for _ in range(test_case_count):
    stk.append(int(input()))

last_height = 0
while len(stk)>=1:
    popped = stk.pop()
    #print(f'{last_height, popped}')
    if last_height < popped :
        #print(f'POPPED: {last_height, popped}')
        last_height = popped
        result += 1
print(result)