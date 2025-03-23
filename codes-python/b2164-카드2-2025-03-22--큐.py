import collections

input_num = int(input())
cards = [ a+1 for a in range(input_num)]
dq = collections.deque(cards)
result = 0

while len(dq) > 1 :
    dq.popleft()
    dq.rotate(-1)
    result += 1

print(dq[0])