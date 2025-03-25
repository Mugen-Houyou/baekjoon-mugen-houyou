import sys
from collections import deque
input = sys.stdin.readline


def get_next_direction(current_dir,upcoming_dir):
    if upcoming_dir == None:    return current_dir # 방향 그대로.

    if snake_current_direction == 'u':
        if upcoming_dir == "L": return 'l'
        else:                   return 'r'
    elif snake_current_direction == 'd':
        if upcoming_dir == "L": return 'r'
        else:                   return 'l'
    elif snake_current_direction == 'l':
        if upcoming_dir == "L": return 'd'
        else:                   return 'u'
    else:
        if upcoming_dir == "L": return 'u'
        else:                   return 'd'
    # 상->L:'left', 상->D:'right'
    # 하->L:'right', 하->D:'left'
    # 좌->L:'down', 좌->D:'up'
    # 우->L:'up', 우->D:'down'


def is_over(new_head, snake_hontai): # True면 게임 망한 것. 
    if new_head in snake_hontai: # 자기 자신을 밟는다
        return True
    for s in new_head: # 벽으로 간다
        if s < 0 or s >= board_size: 
            return True
        
    return False # 다 아니면 생존


# 게임 망했으면 True
def forward(snake_upcoming_direction): # 전진. 사과 먹을 때의 판정 및 조치도 여기서.
    global snake_hontai
    global apple_coords
    global snake_current_direction

    cdr = snake_current_direction # 방향을 결정
    new_head = None # 새 머리

    if cdr == 'u':   new_head = (snake_hontai[-1][0]-1, snake_hontai[-1][1])
    elif cdr == 'd': new_head = (snake_hontai[-1][0]+1, snake_hontai[-1][1])
    elif cdr == 'l': new_head = (snake_hontai[-1][0], snake_hontai[-1][1]-1)
    else:            new_head = (snake_hontai[-1][0], snake_hontai[-1][1]+1)
    
    if is_over(new_head, snake_hontai): return True # 게임 망했으면 True
    
    snake_hontai.append(new_head) # 새 머리 붙이기

    if new_head in apple_coords: # 사과를 먹었으면 그 사과 지움, 안 먹었으면 꼬리를 지움
        apple_coords.remove(snake_hontai[-1])
    else: 
        snake_hontai.popleft()

    snake_current_direction = get_next_direction(snake_current_direction, snake_upcoming_direction) 


# 입력 & 세팅
board_size = int(input())

apple_count = int(input())
apple_coords = [None]*apple_count
for i in range(apple_count): # -1로 저장.
    a,b = map(int,input().split())
    apple_coords[i] = (a-1,b-1)
apple_coords = set(apple_coords)

snake_hontai = deque([(0,0)]) # [-1]이 대가리. [0]이 꼬리.
snake_current_direction = 'r' # 상u, 하d, 좌l, 우r
snake_movement_count = int(input())
snake_set_direction = [None]*10001
for i in range(snake_movement_count):
    time_str, direction = map(str, input().split())
    snake_set_direction[int(time_str)] = direction

# 계산 & 출력
for t in range(1,10001): # 1,2,3, ... 10000. 0초는 이미 지나갔음.
    result = forward(snake_set_direction[t])
    if result: print(t); break
