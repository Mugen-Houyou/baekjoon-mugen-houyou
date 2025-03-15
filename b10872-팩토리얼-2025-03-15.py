# import sys
# input = sys.stdin.readline

""" 
팩토리얼의 정의:
0! = 1
N > 0이면, N! = N * (N-1)!
"""


def fctr_rc(curr_val: int):
    if (curr_val) <= 1:
        return 1;
    else:
        return curr_val * fctr_rc(curr_val-1)

def fctr_it(a):
    result = 1
    for i in range(1,a+1):
        result *=i;
    return result

# print(fctr_it(int(input())))
print(fctr_rc(int(input())))