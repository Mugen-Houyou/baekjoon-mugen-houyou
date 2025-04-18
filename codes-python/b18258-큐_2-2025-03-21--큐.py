from collections import deque
import sys

input = sys.stdin.readline
dq = deque()

for _ in range(int(input())):
    command = input().split()

    if command[0] == 'push':
        param = command[1]
        dq.append(param)
        
    elif command[0] == 'pop':
        if dq: 
            print(dq.popleft())
            # qe = qe[1:]

        else: print(-1)
        
    elif command[0] == 'front':
        if dq: print(dq[0])
        else: print(-1)

    elif command[0] == 'back':
        if dq: print(dq[-1])
        else: print(-1)
        
    elif command[0] == 'size':
        print(len(dq))
        
    elif command[0] == 'empty': 
        if dq: print(0)
        else: print(1)
