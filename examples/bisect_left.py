from bisect import bisect_right

def binary_search_find_lower(arr,target_num): 
    # bisect_left와 동일한 기능 수행
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if  arr[mid] == target_num: return mid
        elif arr[mid] < target_num: low = mid+1
        elif arr[mid] > target_num: high = mid-1
    return low

def binary_search_find_upper(arr, target_num):
    # bisect_right와 동일한 기능 수행
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= target_num: low = mid + 1
        else:                      high = mid - 1
    return low

def binary_search_find_exact(arr,target_num): 
    # 정확한 값을 찾음
    low = 0
    # mid = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if  arr[mid] == target_num: return mid
        elif arr[mid] < target_num: low = mid+1
        elif arr[mid] > target_num: high = mid-1
    return -1

def binary_search_find_mid(arr,target_num): 
    # 얘는 뭘까?
    low = 0
    mid = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if  arr[mid] == target_num: return mid
        elif arr[mid] < target_num: low = mid+1
        elif arr[mid] > target_num: high = mid-1
    return mid

def bs_by_bisect(arr,target_num):
    return bisect_right(arr,target_num)

arr = [10, 20, 50, 66, 123, 214, 333, 444, 555, 777]
print("----------------------")
target_num = 9
print(binary_search_find_lower(arr,target_num), bs_by_bisect(arr,target_num))
target_num = 10
print(binary_search_find_lower(arr,target_num), bs_by_bisect(arr,target_num))
target_num = 11
print(binary_search_find_lower(arr,target_num), bs_by_bisect(arr,target_num))
print("----------------------")
target_num = 49
print(binary_search_find_lower(arr,target_num), bs_by_bisect(arr,target_num))
target_num = 50
print(binary_search_find_lower(arr,target_num), bs_by_bisect(arr,target_num))
target_num = 51
print(binary_search_find_lower(arr,target_num), bs_by_bisect(arr,target_num))
print("----------------------")
target_num = 776
print(binary_search_find_lower(arr,target_num), bs_by_bisect(arr,target_num))
target_num = 777
print(binary_search_find_lower(arr,target_num), bs_by_bisect(arr,target_num))
target_num = 778
print(binary_search_find_lower(arr,target_num), bs_by_bisect(arr,target_num))
print("----------------------")

