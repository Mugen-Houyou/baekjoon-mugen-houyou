input_n = int(input().strip())

count = 0 # 결과
col = [0] * input_n  # 각 행의 퀸의 열 번호의 리스트

# is_safe는 지금 퀸을 놓을 후보 행(=row)과 컬럼(=c)를 받아, 이전에 놓은 퀸들을 하나하나 순회하며 안전한지 검사
def is_safe(row, c):
    result = True
    for i in range(row): # 이전 행들의 퀸들과 충돌하는가? 충돌 즉시 False
        # 같은 컬럼 or 대각선
        if col[i] == c or abs(col[i] - c) == row - i:
            return False
    return result

def backtrack(row):
    global count
    if row == input_n: # 베이스 조건 - 모든 행에 퀸을 놓았으므로 끝
        count += 1
        return
    for c in range(input_n): # 여기서 c는 현재 행에 놓을 후보 컬럼 번호
        if is_safe(row, c):
            col[row] = c
            backtrack(row + 1)

backtrack(0) # 0번째 row부터 시작
print(count)