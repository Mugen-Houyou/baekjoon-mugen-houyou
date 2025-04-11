def gdy_coin():
    nokori = K

    # 블럭 1
    curr_idx = -1 # 5원부터
    coin = coin_types[curr_idx]
    if nokori >= coin:
        for i in range(nokori//coin):
            result.append(coin)
        nokori = nokori % coin
        
    if nokori <= 0: # 잔액 없음
        return len(result)
    
    curr_idx = 0 # 이제 2원
    # 있으면 계속 뺌
    while nokori%coin_types[curr_idx] != 0 and result:
        nokori += result.pop()

    # 블럭 2
    coin = coin_types[curr_idx]
    if nokori >= coin:
        for i in range(nokori//coin):
            result.append(coin)
        nokori = nokori % coin
        
    if nokori <= 0: # 잔액 없음
        return len(result)
    else: 
        return -1
    
    # 이런 식으로 반복 ... ==> 동전 3개 이상이면 블럭을 while로 묶기
    while nokori%coin_types[curr_idx] != 0 and result:
        nokori += result.pop()
    
    


# 입력 & 세팅
K = int(input())
coin_types = [2,5]
result = []

# 처리 & 출력
print(gdy_coin())
