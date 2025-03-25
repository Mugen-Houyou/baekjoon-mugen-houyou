def binary_search_lower_bound(arr,target_num):
    low = 0
    # mid = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2
        if  arr[mid] == target_num: return mid
        elif arr[mid] < target_num: low = mid+1
        elif arr[mid] > target_num: high = mid-1

    return low

input_count = int(input())
input_list = list(map(int,input().split()))
max_last = 0
result_list = []

result_list = [input_list[0]]
for i in range(1, len(input_list)):
    #print("BEGIN",result_list)
    if input_list[i] > result_list[-1]:
        result_list.append(input_list[i])
    else:
        index = binary_search_lower_bound(result_list, input_list[i])
        result_list[index] = input_list[i]
    #print("DONE",result_list)


print(f'인덱스: {binary_search_lower_bound(input_list,34)} / 값: {input_list[binary_search_lower_bound(input_list,34)]}')

# print(len(result_list))