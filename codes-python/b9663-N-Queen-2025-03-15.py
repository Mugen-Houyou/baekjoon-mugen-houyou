size = int(input())
board = [[False for _ in range(size)] for _ in range(size)] # 

def is_legit_placement(size,ax,ay,bx,by): # 2개의 퀸의 좌표를 입력받아, 정당한 배치인지?
    # i) x좌표 검증
    if ax==bx: return True
    # ii) y좌표 검증
    if ay==by: return True
    # iii) 대각선 검증
    if ax-bx == ay-by: return True
    return False 

# board[2][5] = True

for i in board:
    for j in i:
        print(j,end="")
    print()
