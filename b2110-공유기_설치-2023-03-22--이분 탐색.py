import sys
input = sys.stdin.readline
house_count, router_count = map(int,input().split())
house_coords = []
result_list = []

for _ in range(house_count):
    house_coords.append(int(input()))

def find_mid(curr_min,curr_max):
    high = curr_max
    mid = 0
    low = curr_min

    
    

    return

h_max = max(house_coords) 
h_min = min(house_coords)

# 우선 2, 3개라도 구현
if router_count == 2:
    print(h_max-h_min)
elif router_count == 3:
    h_mid = find_mid(h_min, h_max)
    print(min(h_max-h_mid, h_mid-h_min))