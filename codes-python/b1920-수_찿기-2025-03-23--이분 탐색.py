number_count = int(input())
database = sorted(map(int,input().split()))
find_count = int(input())
to_finds = map(int,input().split())

# print(number_count,database,find_count,to_finds)
"""
<이분 탐색의 수도코드>

    먼저, 찾는 숫자 target; low=0; high=len(arr)-1로 세팅

    while (low<=high); mid=(low+high)//2;
        만약 arr[mid] == target면; return mid (∵ 값을 찾음)
        만약 arr[mid] < target면; low=mid+1 (∵ 하방을 갱신)
        만약 arr[mid] > target면; high=mid-1 (∵ 상방을 갱신)

    만약 while문을 다 돌았으면; target는 arr에 없음
"""
def binary_search(target_num):
    low = 0
    high = len(database)-1

    while low <= high:
        mid = (low+high)//2
        if  database[mid] == target_num: return mid
        elif database[mid] < target_num: low=mid+1
        elif database[mid] > target_num: high=mid-1
    
    return -1

def bs_recursive(target_num, low=0, high=None):
    if high is None: high=len(database)-1
    if low>high: return -1

    mid = (low+high)//2

    if  database[mid] == target_num: return mid
    elif database[mid] < target_num: return bs_recursive(target_num, mid+1, high)
    elif database[mid] > target_num: return bs_recursive(target_num, low, mid-1)

def binary_search_exists(target_num):
    low = 0
    high = len(database)-1

    while low <= high:
        mid = (low+high)//2
        if  database[mid] == target_num: return 1
        elif database[mid] < target_num: low=mid+1
        elif database[mid] > target_num: high=mid-1
    
    return 0

for t in to_finds:
    print(binary_search_exists(t))
