import sys
input = sys.stdin.readline
house_count, router_count = map(int,input().split())
house_coords = []

for _ in range(house_count):
    house_coords.append(int(input()))
house_coords.sort()
    
def total_placeable_router_count(min_distance):
    count = 1
    current_house=house_coords[0]
    for i in range(1,len(house_coords)):
        if house_coords[i] >= current_house + min_distance:
            current_house = house_coords[i]
            count += 1
    return count

def binary_search():
    low = 1
    mid = 0
    high = house_coords[-1] - house_coords[0]
    result = 0

    while low <= high:
        mid = (low+high)//2
        if total_placeable_router_count(mid) >= router_count:
            low = mid+1
            result = mid # `result` 변수는 "조건을 만족하는 중에서 가장 큰 `mid`값"을 기록해두는 역할을 하며, 이를 통해 최종적으로 올바른 답을 반환할 수 있게 됨.
        else: 
            high = mid-1 # `result`를 따로 두지 않으면, 다음에 여기로 들어와서, `mid`값이 조건을 만족하지 않게 될 수도 있음.

    return result

print(binary_search())
