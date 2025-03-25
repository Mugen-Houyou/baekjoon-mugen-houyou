import sys
input = sys.stdin.readline

def calculate_max_area(stack, current_index, new_height):
    """
    스택에 있는 막대들 중에서, 새 막대(new_height)보다 높이가 큰 막대들에 대해
    각 막대가 만들 수 있는 영역을 계산하고, pop하면서 최대 영역과 새로운 시작 인덱스를 반환합니다.
    
    파라미터들:
        stack: (시작 인덱스, 높이) 쌍을 담고 있는 스택.
        current_index: 현재 막대가 등장한 인덱스.
        new_height: 현재 막대의 높이.
        
    리턴들:
        local_max: 새 막대에 의해 pop된 막대들로 계산한 영역 중 최대값.
        start: 새 막대를 삽입할 때 사용할 시작 인덱스 (pop된 막대들 중 가장 왼쪽 인덱스).
    """
    local_max = 0
    start = current_index
    while stack and stack[-1][1] > new_height:
        idx, height = stack.pop()
        # 해당 막대(height)가 current_index까지 확장될 때의 영역
        area = height * (current_index - idx)
        local_max = max(local_max, area)
        start = idx  # pop된 막대의 시작 인덱스를 갱신하여, 이후 새 막대와 결합 가능하게 함
    return local_max, start

while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    n = data[0]
    heights = data[1:]
    
    max_area = 0
    stack = []
    
    # 각 막대를 순회하면서 처리
    for i, h in enumerate(heights):
        if stack and stack[-1][1] > h:
            # 현재 막대가 스택 최상단보다 낮은 경우,
            # calculate_max_area 함수로 스택에서 pop하며 영역 계산
            local_max, start = calculate_max_area(stack, i, h)
            max_area = max(max_area, local_max)
            stack.append((start, h))
        else:
            # 현재 막대가 스택에 있는 막대보다 크거나 스택이 비어있으면 그냥 삽입
            stack.append((i, h))
    
    # 모든 막대 처리 후, 스택에 남은 막대들에 대해 히스토그램 끝까지 확장 가능한 영역 계산
    total_length = len(heights)
    while stack:
        idx, height = stack.pop()
        max_area = max(max_area, height * (total_length - idx))
    
    print(max_area)






# import sys
# input=sys.stdin.readline

# def calculate_max_area(stk, height): # 이 스택에서 나올 수 있는 가장 큰 영역
#     tmp_height=height
#     i = 1
#     while stk:
#         tmp_pop = stk.pop()

#         # 더 낮은 값이 나와버리면 
#         i += 1
        






#         tmp_height = stk.pop()



#     else: return 0

# while True:
#     input_str = input()
#     if input_str == "0" or input_str == 0: exit()

#     last_max_area = 0
#     input_list = list(map(int,input_str.split()))[1:]
#     stk = []
    
#     for i in range(len(input_list)):
#         if len(stk)==0: 
#             stk.append(input_list[i])
#             continue

#         if input_list[i] < stk[-1]: # 더 작아짐, 즉 개변 필요.
#             last_max_area = max( last_max_area, calculate_max_area(stk,input_list[i]) )
#             stk.clear()
#             stk.append(input_list[i])
#         else:
#             stk.append(input_list[i])

#     if stk: last_max_area = max( last_max_area, calculate_max_area(stk) )
#     print(last_max_area)
