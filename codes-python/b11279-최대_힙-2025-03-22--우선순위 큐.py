import heapq
import sys
input = sys.stdin.readline

case_count = int(input())
hpq = []

for _ in range(case_count):
    command = -int(input())
    if command == 0: 
        if hpq:
            print(-heapq.heappop(hpq))
        else: 
            print(0)
    else: 
        heapq.heappush(hpq, command)
