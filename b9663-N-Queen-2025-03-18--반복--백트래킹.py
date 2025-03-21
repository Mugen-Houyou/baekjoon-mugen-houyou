def solve():
    import sys
    input = sys.stdin.readline
    N = int(input().strip())
    
    count = 0
    # 각 행에 놓은 퀸의 열 번호를 저장할 리스트
    col = [0] * N  
    row = 0  # 현재 놓으려는 행
    
    while row >= 0:
        # 현재 행에서 모든 열을 시도했으면 backtracking
        if col[row] >= N:
            col[row] = 0
            row -= 1
            if row >= 0:
                col[row] += 1  # 이전 행의 퀸 위치를 옮겨 다음 열 시도
        else:
            valid = True
            # 이전 행들에 놓인 퀸과 충돌하는지 확인 (같은 열 또는 대각선)
            for i in range(row):
                if col[i] == col[row] or abs(col[i] - col[row]) == row - i:
                    valid = False
                    break
            if valid:
                if row == N - 1:
                    # 마지막 행에 도달하여 유효한 배치인 경우
                    count += 1
                    col[row] += 1  # 같은 행에서 다음 열을 시도
                else:
                    # 다음 행으로 진행
                    row += 1
                    col[row] = 0
            else:
                # 현재 열 위치가 안전하지 않으면, 다음 열로 시도
                col[row] += 1

    print(count)

if __name__ == '__main__':
    solve()
