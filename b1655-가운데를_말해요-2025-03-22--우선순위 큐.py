import sys
import heapq
input=sys.stdin.readline

case_count = int(input())
lhpq = []
rhpq = []


"""
0. 좌측 힙은 최대힙 (즉, 부호를 반대로), 우측 힙은 최소힙으로 구성.

1. 양 힙의 길이가 같음?
    1-1. 그렇다면, 왼쪽 힙에 요소*(-1)을 삽입.
    1-2. 그렇지 않다면, 오른쪽 힙에 요소를 삽입.

2. 양 힙에 요소가 존재 && 왼쪽 힙의 첫요소*(-1)가 오른쪽 첫요소보다 큼?
    2-1. 그렇다면, 왼쪽 힙의 첫요소와 오른쪽 힙의 첫요소를 교체. (둘 다 꺼내서, 둘 다 부호 바꿔서, 교체)

3. 왼쪽 힙의 첫요소*(-1)를 출력.
"""


for _ in range(case_count):
    el = int(input())

    if len(lhpq) == len(rhpq):
        heapq.heappush(lhpq,-el)
    else:
        heapq.heappush(rhpq,el)
    
    if lhpq and rhpq and -lhpq[0] > rhpq[0]:
        left_tmp = heapq.heappop(lhpq)
        right_tmp = heapq.heappop(rhpq)

        heapq.heappush(lhpq,-right_tmp)
        heapq.heappush(rhpq,left_tmp)

    print(f'중간 결과: {lhpq,rhpq}')   
    print(-lhpq[0])

