count, target_num = map(int,input().split())
trees = list(map(int,input().split()) )



def cut_all_and_return_sum(result_h):
    global trees
    sum=0
    for i in range(len(trees)): # 모든 나무를 자르기
        if trees[i]-result_h >= 0: 
            sum += trees[i]-result_h
    return sum
    

def recur(result_h):
    
    if cut_all_and_return_sum() > target_num: # h를 높여야 함
        recur()
    elif: 
    
    else:


    return

recur( max(trees))
# print(result_h)