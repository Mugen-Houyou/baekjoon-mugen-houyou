input_count = int(input())
input_list = [ int(a) for a in input().split()]
result_list = [0]*input_count

for i in reversed(range(input_count)): # 4,3,2,1,0
    for j in reversed(range(0,input_count-i-1)): # i=0->3,2,1,0, i=1->2,1,0
        if input_list[i] <= input_list[j]:
            result_list[i] = j+1
            break

while result_list: # pop()로 역순으로 출력
    print(result_list.pop(),end=" ")