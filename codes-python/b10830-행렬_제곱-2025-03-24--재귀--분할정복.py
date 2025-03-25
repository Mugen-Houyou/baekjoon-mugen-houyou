def dot_product(input_matrix_a, input_matrix_b, row, col):
    # 행렬 곱셈 중, 특정 row와 col의 곱셈 과정을 따로 뺀 함수임.
    return sum(
        input_matrix_a[row][i]*input_matrix_b[i][col] for i in range(len(input_matrix_a))
        )

def matrix_mul(input_matrix_a, input_matrix_b):  
    result = [[None]*len(input_matrix_a) for _ in range(len(input_matrix_a))]

    for row in range(len(input_matrix_a)):
        for col in range(len(input_matrix_a)):
            result[row][col] = dot_product(input_matrix_a, input_matrix_b, row, col) % 1000
    
    return result
    
def matrix_pow(input_matrix, input_power):  
    if input_power == 1: # 그냥 리턴하면 안됨! 인풋된 원소들 중에 1000이 있으면 그냥 1000이 나와버리므로.
        return [[value % 1000 for value in row] for row in input_matrix]

    half = matrix_pow(input_matrix, input_power//2)
    
    if input_power%2 == 0:
        return matrix_mul(half, half)
    else:
        return matrix_mul(matrix_mul(half, half), input_matrix)


# 입력 & 세팅
matrix_size , power_val = map(int,input().split())
matrix = [None]*matrix_size
for i in range(matrix_size):
    matrix[i] = list(map(int,input().split()))

# 계산
result = matrix_pow(matrix,power_val)

# 출력
for i in range(len(result)):
    print(*result[i])


""" 아래는 1629 곱셈 분할정복 코드의 예시
def multiplier(a,b,c):                                  # 예: b=3
    if b==1:        return a%c                          # b==3일 경우 스킵

    mul_result = multiplier(a, b//2, c)                 # multiplier(a,1,c) ==> a % c를 가져옴

    if b%2 == 0:    return (mul_result*mul_result)%c    # b==3일 경우 스킵
    else:           return (mul_result*mul_result*a)%c  # (multiplier(a,1,c)*multiplier(a,1,c)*a) % c
"""