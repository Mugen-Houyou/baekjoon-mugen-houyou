"""
KOI 사냥터에는 N 마리의 동물들이 각각 특정한 위치에 살고 있다. 사냥터에 온 사냥꾼은 일직선 상에 위치한 M 개의 사대(총을 쏘는 장소)에서만 사격이 가능하다. 편의상, 일직선을 x-축이라 가정하고, 사대의 위치 x1, x2, ..., xM은 x-좌표 값이라고 하자. 각 동물이 사는 위치는 (a1, b1), (a2, b2), ..., (aN, bN)과 같이 x,y-좌표 값으로 표시하자. 동물의 위치를 나타내는 모든 좌표 값은 양의 정수이다.

사냥꾼이 가지고 있는 총의 사정거리가 L이라고 하면, 사냥꾼은 한 사대에서 거리가 L 보다 작거나 같은 위치의 동물들을 잡을 수 있다고 한다. 단, 사대의 위치 xi와 동물의 위치 (aj, bj) 간의 거리는 |xi-aj| + bj로 계산한다.

예를 들어, 아래의 그림과 같은 사냥터를 생각해 보자. (사대는 작은 사각형으로, 동물의 위치는 작은 원으로 표시되어 있다.) 사정거리 L이 4라고 하면, 점선으로 표시된 영역은 왼쪽에서 세 번째 사대에서 사냥이 가능한 영역이다.

사대의 위치와 동물들의 위치가 주어졌을 때, 잡을 수 있는 동물의 수를 출력하는 프로그램을 작성하시오.

"""
from bisect import bisect_left
import sys
input = sys.stdin.readline

shooter_count, animal_count, shot_range = map(int,input().split())
shooter_coords = sorted(map(int,input().split()))
animal_coords = [[a for a in map(int,input().split())] for _ in range(animal_count)]
result = 0

def bileft_shooter(shooter_coords, target_x_coord):
    # target_x_coord가 삽입될 인덱스를 리턴 (즉, 가장 가까운 "오른쪽" 후보의 인덱스)
    # 例) shooter_coords = [2, 5, 8]이고, target_x_coord = 6 ==> 리턴값은 2, 즉, 값으로 보면 8이 있는 자리를 리턴. 만약 [2, 5, 6, 8]이면 2 리턴 (즉, 정확히 6이 있는 자리)
    return bisect_left(shooter_coords, target_x_coord)

def binary_search_shooter(shooter_coords, animal_x_coord):
    # 가장 가까운 (듯한) 사냥꾼 검색
    low = 0
    mid = 0
    high = len(shooter_coords)-1
    while low<=high:
        mid = (low+high)//2
        if  shooter_coords[mid] == animal_x_coord: return mid
        elif shooter_coords[mid] < animal_x_coord: low  = mid+1
        elif shooter_coords[mid] > animal_x_coord: high = mid-1
    return mid

def is_reachable(shooter_coord, animal_x_coord, animal_y_coord, shot_range):
    # 사냥 시도
    # 단, 사대의 좌표가 무효할 경우 그냥 False.
    if shooter_coord <= 0: return False
    return abs(shooter_coord - animal_x_coord) + animal_y_coord <= shot_range

for x, y in animal_coords:
    s_idx = binary_search_shooter(shooter_coords, x)
    
    if is_reachable(shooter_coords[s_idx], x, y, shot_range):
        try:
            result += 1
        except:
            continue
    else: # 안돼? 그러면 좌, 우 사대에게 한번 시켜본다.
        minus_one_coord = -sys.maxsize
        plus_one_coord = -sys.maxsize

        try: minus_one_coord = shooter_coords[s_idx-1]
        except: pass
        try: plus_one_coord = shooter_coords[s_idx+1]
        except: pass

        if is_reachable(minus_one_coord, x, y, shot_range):
            result += 1
        elif is_reachable(plus_one_coord, x, y, shot_range):
            result += 1

print(result)
