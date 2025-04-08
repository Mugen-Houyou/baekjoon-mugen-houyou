import sys
INF = 1<<31

def gdy_meetings():
    # sch_parseds에 (시작,종료)로 파싱
    # 정렬! 먼저 종료시각 기준 => 같으면 시작시각 기준
    sch_parseds = sorted(
            [list(map(int, sch.split())) for sch in schedules], 
            key=lambda x: (x[1], x[0])
        )

    result = [(0,0)] 
    curr_end = 0 # 선택했었던 방의 종료시각
    
    for start, end in sch_parseds:
        if start >= result[-1][1]:
            result.append((start,end))

    return len(result)-1


input_list = sys.stdin.read().strip().split("\n")
N = int(input_list[0])
schedules = input_list[1:]

#print(N,schedules)
print(gdy_meetings())
