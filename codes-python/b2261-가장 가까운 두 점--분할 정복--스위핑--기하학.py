import sys
input = sys.stdin.readline

n = int(input())
coords = [list(map(int, input().split())) for _ in range(n)]
coords.sort(key=lambda x: x[0]) # x좌표 기준 정렬

def calc_dist_sqrd(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def solution(l_idx, r_idx):
    if l_idx == r_idx:   return float('inf')                                 # 점이 하나뿐인 경우.
    if l_idx+1 == r_idx: return calc_dist_sqrd(coords[l_idx], coords[r_idx]) # 구간에 2개밖에 없는 경우.

    mid = (l_idx+r_idx)//2
    lv = solution(l_idx, mid)
    rv = solution(mid, r_idx)

    result = min(lv, rv)

    # 중간 영역 확장
    for i in range(l_idx, mid+1): 
        for j in range(mid+1, r_idx+1):
            temp_dist = calc_dist_sqrd(coords[i], coords[j])
            result = min(result, temp_dist)
    
    return result

def solution_impvd(l_idx, r_idx):
    if l_idx == r_idx:   return float('inf')                                 # 점이 하나뿐인 경우.
    if l_idx+1 == r_idx: return calc_dist_sqrd(coords[l_idx], coords[r_idx]) # 구간에 2개밖에 없는 경우.

    mid = (l_idx+r_idx)//2
    lv = solution_impvd(l_idx, mid)
    rv = solution_impvd(mid, r_idx)

    # 아직까지는 좌우만 반영한 최소
    result = min(lv, rv)
    
    # y좌표 기준 스캔 및 추가
    candis_y = []
    for i in range(l_idx,r_idx+1): # r_idx도 포함해야 하므로.
        if (coords[mid][0]-coords[i][0])**2 < result: # x좌표만 반영한 거리
            candis_y.append(coords[i])

    # y좌표로 추린 리스트에서 최소 거리 구하기
    candis_y.sort(key=lambda x:x[1]) # y좌표 기준 정렬
    for i in range(len(candis_y)-1):
        for j in range(i+1, len(candis_y)):
            if (candis_y[i][1] - candis_y[j][1])**2 < result: # y좌표만 반영한 거리
                result = min(
                    result, calc_dist_sqrd(candis_y[i], candis_y[j])
                    )
            else: 
                break

    return result

print(solution_impvd(0, n-1)) # n개이니까 인덱스는 0부터 n-1까지.