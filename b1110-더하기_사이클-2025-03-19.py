input_num = int(input())
if 0<= input_num <10:
    if input_num==0:
        print(1)
        exit()
    input_num = input_num + input_num*10
orig_num = input_num

result=0
while True:
    sum_digit = 0
    for i in str(input_num):
        sum_digit += int(i)
    new_num = int(str(input_num)[-1]+str(sum_digit)[-1])
    result += 1
    input_num = new_num
    if new_num == orig_num:
        print(result)
        exit()