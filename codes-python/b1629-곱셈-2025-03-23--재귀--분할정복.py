import sys
input = sys.stdin.readline

def multiplier(a,b,c):                                  # 예: b=3
    if b==1:        return a%c                          # b==3일 경우 스킵

    mul_result = multiplier(a, b//2, c)                 # multiplier(a,1,c) ==> a % c를 가져옴

    if b%2 == 0:    return (mul_result*mul_result)%c    # b==3일 경우 스킵
    else:           return (mul_result*mul_result*a)%c  # (multiplier(a,1,c)*multiplier(a,1,c)*a) % c

# a의 b제곱, c의 나머지.
print(multiplier(*map(int,input().split())))