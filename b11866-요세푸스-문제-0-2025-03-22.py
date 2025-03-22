import collections

n, k = map(int,input().split())
people = collections.deque([p+1 for p in range(n)]) # 사람 번호 겸 인덱스
killed_list = collections.deque()

def josephus ():
    people.rotate(-k)
    killed_list.append(people.pop())
    return False

while len(killed_list) < n:
    if josephus(): break

print("<",end="")
for i in range(len(killed_list)):
    print(killed_list[i],end="")
    if i != len(killed_list)-1:
        print(", ",end="")
print(">",end="")

