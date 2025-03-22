input_count = int(input())
input_list = [ int(a) for a in input().split()]
index_stk = [] # 값 자체가 아니라 인덱스를 넣는다!

def jfc(current_idx):
    if current_idx < 0 or current_idx>len(input_list)-1:
        return
    
    if len(index_stk)==0:
        index_stk.append(current_idx)
        print(0,end=" ")
        return

    if input_list[index_stk[-1]] < input_list[current_idx]: # 여전히 새 값이 크다!
        index_stk.pop()
        jfc(current_idx)
        
    elif input_list[index_stk[-1]] == input_list[current_idx]: # 서로 같음!
        print(current_idx + 1,end=" ")
        index_stk.append(current_idx)

    else:
        print(index_stk[-1]+ 1 ,end=" ")
        index_stk.append(current_idx)

for i in range(input_count):
    jfc(i)
