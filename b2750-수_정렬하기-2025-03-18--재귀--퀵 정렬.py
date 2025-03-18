# 내장 라이브러리 안 씀
# 퀵 정렬 구현
import sys
input=sys.stdin.readline

def qs_start (ls):
    qs(ls, 0 ,len(ls)-1)

def qs (ls, left_starting_point, right_starting_point):    
    pivot = ls[(left_starting_point + right_starting_point) // 2]
    cur_left = left_starting_point
    cur_right = right_starting_point

    # 퀵 핵심부
    while cur_left <= cur_right:
        # 위치 세팅
        while ls[cur_left] < pivot : cur_left += 1
        while ls[cur_right] > pivot : cur_right -= 1
        print(f'{ls}, {cur_left},{cur_right} ')
        # 스왑
        if cur_left <= cur_right:
            ls[cur_left], ls[cur_right] = ls[cur_right], ls[cur_left] 
            cur_left += 1
            cur_right -= 1
    
    # 좌측 재귀 (이 함수의 좌측 시작점부터, 현재 우측 커서까지)
    if left_starting_point < cur_right : qs(ls, left_starting_point, cur_right)
    # 우측 재귀 (이 함수의 현재 좌측 커서부터, 우측 시작점까지)
    if cur_left < right_starting_point : qs(ls, cur_left, right_starting_point)

# 입력
# ls = [None]*int(input())
# for i in range(len(ls)):
#     ls[i] = int(input())
ls = [3,2,4,1,0,5,7,6,8,9]

# 정렬
qs_start(ls)


for l in ls:
    print(l)