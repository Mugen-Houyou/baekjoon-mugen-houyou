size = int(input())
size_exp = size.bit_length()-1

board = [ None]*size
for i in range(size):
    board[i] = input()

def is_all_same(start_row,start_col,end_row,end_col):
    starting_char = board[start_row][start_col]
    for r in range(start_row,end_row+1):
        for c in range(start_col,end_col+1):
            if board[r][c] != starting_char: return False
    return True

def quad_tree(se,start_row,start_col,end_row,end_col) -> str:
    
    # 더 못 쪼개도 상관없다, 왜냐면 is_all_same()가 항상 True를 반환할 테니까.
    if is_all_same(start_row,start_col,end_row,end_col):
        result = board[start_row][start_col]
    else:
        result = "(" 
        qdrt1 = quad_tree(se-1, start_row, start_col, end_row-(2**(se-1)), end_col-(2**(se-1))) # 1사 
        qdrt2 = quad_tree(se-1, start_row, start_col+(2**(se-1)), end_row-(2**(se-1)), end_col) # 2사
        qdrt3 = quad_tree(se-1, start_row+(2**(se-1)), start_col, end_row, end_col-(2**(se-1))) # 3사
        qdrt4 = quad_tree(se-1, start_row+(2**(se-1)), start_col+(2**(se-1)), end_row, end_col) # 4사
        result = "("  + qdrt1+qdrt2+ qdrt3+ qdrt4+")"
    return result

print(quad_tree(size_exp,0,0,size-1,size-1))