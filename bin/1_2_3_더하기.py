T = int(input())
 # # ##  팩토리얼 사용하면 경우의 수 구할 수 있다! 
 
def plus_one_two_three(T):
    num_list = list(map(int, input().split()))
    
    for i in range(T):
        
        count = 0
        for j in num_list: 
            # 같은 숫자가 K번 반복되는 경우 
                
            
            for k in range(1, k):
                # 같은 숫자가 1번 반복되는 경우 
                count += factory(j) / (factory(1) + factory(2))
                ### 아아앙아아앙 ㅏ
            # 1로만 이루어진 경우 
            count += 1
            #1과 2로만 이루어진 경우
            count += factory(j) / (factory(1) + factory(2))
            # 1과 3으로 이루어진 경우 
            count += factory(j) / (factory(1) + factory(3))
            # 1,2,3으로 이루어진 경우 
            count += factory(j) / (factory(1) + factory(3) + factory(2))
            # 2로만 이루어진 경우
            if j % 2 == 0:
                count += (factory(j) / factory(2))
            #3으로만 이루어진 경우 
            if j % 3 == 0:
                count += (factory(j) / factory(3))
            return count

def factory(num):
    sum = 1
    for i in range(1, num ):
        print(i)
        sum += sum * i
    return sum


print(plus_one_two_three(T))