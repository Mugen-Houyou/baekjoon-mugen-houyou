input_str = input().strip()
stk = []
result = 0
multiplier_v = 1

for i, c in enumerate(input_str):
    if c == '(':
        multiplier_v *= 2
        stk.append(c)

    elif c == '[':
        multiplier_v *= 3
        stk.append(c)

    elif c == ')':
        if not stk or stk[-1] != '(':
            print(0)
            exit(0)
        try:
            if input_str[i-1] == '(': # 즉, 최고 레벨인 지점에서 정산.
                result += multiplier_v
        except: # 이걸 못한다? 안되는 괄호식이다.
            print(0)
            exit(0)
        stk.pop() # pop하기!
        multiplier_v //= 2

    elif c == ']':
        if not stk or stk[-1] != '[':
            print(0)
            exit(0)
        try:
            if input_str[i-1] == '[': # 즉, 최고 레벨인 지점에서 정산.
                result += multiplier_v
        except: # 이걸 못한다? 안되는 괄호식이다.
            print(0)
            exit(0)
        stk.pop() # pop하기!
        multiplier_v //= 3

if stk: # 뭐가 남으면 안됨.
    print(0)
    exit(0)

print(result)
