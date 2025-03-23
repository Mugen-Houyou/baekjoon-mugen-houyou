import sys
input = sys.stdin.readline
stk = []

for _ in range(int(input())):
    command = input().split()
    if command[0] == 'push':
        param = command[1]
        stk.append(param) 
    elif command[0] == 'pop':
        if len(stk) == 0: print(-1)
        else: 
            print(stk[len(stk)-1])
            stk = stk[:-1]
    elif command[0] == 'top':
        if len(stk) == 0: print(-1)
        else: 
            print(stk[-1])
    elif command[0] == 'size':
        print(len(stk))
    elif command[0] == 'empty': 
        if len(stk) == 0: print(1)
        else: print(0)