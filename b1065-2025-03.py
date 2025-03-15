def is_hansu(num):
    str_num = str(num)
    if len(str_num)<= 2: 
        return True
    interval = int(str_num[1])-int(str_num[0])
    for i in range(len(str_num[:-1])):
        if int(str_num[i])+interval != int(str_num[i+1]):
            return False;
    return True
    
# result = len([is_hansu(j) for j in range(1,int(input())+1)]) # 틀린 list comprehension
result = sum(is_hansu(j) for j in range(1,int(input())+1))
# result = len([j for j in range(1, int(input())+1) if is_hansu(j)])
print(result)