stk = []
for _ in range(int(input())):
    num = int(input())
    if num == 0:
        stk = stk[:-1]
    else: 
        stk.append(num)
print(sum(stk))
