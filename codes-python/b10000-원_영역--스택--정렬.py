
import sys
input = sys.stdin.readline

# 입력 읽기
circle_count = int(input().strip())
circles = [] 

for _ in range(circle_count):
    x, r = map(int, input().split())    # 좌표와 반지름 정보를 입력받아
    circles.append((x - r, -1))         # 원의 좌경계점 저장 (`,-1`이 좌)
    circles.append((x + r, 1))          # 원이 우경게점 저장 (`,1`이 우)

circles.sort(key=lambda p: 
             (p[0], -p[1]))             # 정렬: 좌표 오름차순, 좌표가 같으면 두 번째 값(상태)가 내림차순

stk = []                                # 스택: 각 항목은 [coord, state], circles를 순회하면서 stk이 비어있으면 항목을 넣고, 그렇지 않은 경우 left_or_right(-1 또는 1)에 따라 stk을 pop하여 state를 갱신한 후, 다시 넣거나, answer를 증가시킴


answer = 0
last = 0

for coord, left_or_right in circles:
    if not stk:
        stk.append([coord, 0])
        last = coord
    elif left_or_right == -1:
        if coord == last:
            # 스택의 top 항목을 꺼내서 state가 -1이 아니면 1로 바꾼 후 다시 push
            tmp = stk.pop()
            if tmp[1] != -1:
                tmp[1] = 1
            stk.append(tmp)
            stk.append([coord, 0])
        else:
            tmp = stk.pop()
            tmp[1] = -1
            stk.append(tmp)
            stk.append([coord, 0])
            last = coord
    elif left_or_right == 1:
        tmp = stk.pop()
        if tmp[1] == 1 and last == coord:
            answer += 2
        else:
            answer += 1
        last = coord

print(answer + 1)