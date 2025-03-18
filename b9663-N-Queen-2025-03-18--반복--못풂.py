
def pi_board():
    for b in board:
        print(b)
    input()
    
init_size = int(input())
board = [[False for _ in range(init_size)] for _ in range(init_size)]

# 각 row마다 반복
row = 0
prev_col = []
# 이전 column 기억
while True:
    # Q 놓기 - 모든 row, col, 대각선으로도
    col=0
    while True:
        # 놓을 수 없으면 생략
        if board[row][col] == True: continue
        
        # 이 row의 모든 col이 True면 포기, 1 row 후퇴, 1 col 생략
        gave_up = True
        for col in board[row]:
            if board[row][col] == False: gave_up = False
        if gave_up == True: 
            board[row-1][prev_col.pop()] = True
            row = row-1
            continue;

        # 놓기 핵심 - 일단 현재 col 기억
        prev_col.append(col)

        # row 전체
        board[row] = [True]*init_size
        # col 전체
        for i in range(init_size):
            board[i][col] = True
        # 대각선 전체
        for i in range(init_size):
            pi_board()
            # 우하향 대각선
            # i 증가
            if not( (row+i) > (init_size-1) or (col+i) > (init_size-1) ): 
                print(f"i b{row+i} {col+i}")
                board[row+i][col+i] = True
            # i 감소
            if not( (row-i) < 0 or (col-i) < 0 ): 
                board[row-i][col-i] = True

            # 우상향 대각선
            # 증,감
            if not( (row+i) > (init_size-1) or (col-i) < 0) : 
                board[row+i][col-i] = True
            # 감,증
            if not( (row-i) < 0 or (col+i) > (init_size-1)) : 
                board[row-i][col+i] = True
        input("COL DONE")
        col +=1
        if col >= init_size: break

    row +=1
    if row >= init_size: break
print(board)



