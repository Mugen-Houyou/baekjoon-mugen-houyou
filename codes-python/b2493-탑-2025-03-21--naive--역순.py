input_count = int(input())
input_list = [ int(a) for a in input().split()][::-1]
result_list = [0]*input_count

for i in range(input_count):
    for j in range(i+1,input_count):
        if input_list[i] <= input_list[j]:
            #print(f'{i, input_list[i], j, input_list[j] }')
            result_list[i] = input_count-j
            break
        
for rr in result_list[::-1]:
    print(rr, end=" ")