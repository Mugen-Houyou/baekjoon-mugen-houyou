import sys
from bisect import bisect
input = sys.stdin.readline

def binary_search(arr,target_num):
    low=0
    # mid=0
    high=len(arr)-1
    
    while low <= high:
        mid = (low+high)//2
        if  arr[mid] == target_num: return 1
        elif arr[mid] < target_num: low=mid+1
        elif arr[mid] > target_num: high=mid-1

    return 0

cards_count = int(input())
cards_in_pkt = sorted(map(int,input().split()))
tests_count = int(input())
tests = list(map(int,input().split()))

for i in range(tests_count):
    print(binary_search(cards_in_pkt,tests[i]), end=" ")

# result = [1 if a in cards_in_pkt else 0 for a in tests]
# print(*result)