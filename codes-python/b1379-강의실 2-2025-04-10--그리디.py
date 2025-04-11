import sys
import heapq
INF = 1<<59

def gdy_clsr():
    lectures = sorted(
            [tuple(map(int, asdfasdf.split())) for asdfasdf in input_str[1:]], 
            key=lambda x: (x[1], x[2])  # 번호, 시작시각, 종료시각
        )
    
    hq = [] # 최소 힙 (종료시각, 호실)
    room_count = 0
    result = [0]*(N+1)

    for lecture_id, start, end in lectures:
        if hq and hq[0][0] <= start: # 현재 가장 빨리 끝나는 강의가 끝났다면 (종료시각 <= 지금꺼 시작시각) 
            _, room = heapq.heappop(hq) # 해당 강의실 사용 가능
            result[lecture_id] = room
        else: # 강의실 없음 => 새 호실 배정
            room_count += 1
            room = room_count
            result[lecture_id] = room
        
        heapq.heappush(hq, (end, room))
    
    print(room_count)
    for i in range(1, N+1):
        print(result[i])

# 입력 & 세팅
input_str = sys.stdin.read().strip().split("\n")
N = int(input_str[0])

# 처리 & 출력
gdy_clsr()

