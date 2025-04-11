# 그리디 문제!
import sys

def gdy_coin():
    i = len(coin_types)-1
    nokori = K
    while True:
        coin = coin_types[i]
        if nokori >= coin:
            result.append((coin, nokori//coin))
            nokori = nokori % coin
        else:
            i -= 1
        if nokori <= 0 or i < 0: 
            break
        
    return sum(result[i][1] for i in range(len(result)))


# 입력 & 세팅
input_str=sys.stdin.read().strip().split("\n")
N, K = map(int,input_str[0].split()) # 동전의 종류 N, 목표합 K원
coin_types = list(map(int,input_str[1:]))
result = [] # 사용된 동전 리스트

# 처리 & 출력
print(gdy_coin())
