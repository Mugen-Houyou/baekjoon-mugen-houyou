import sys
input = sys.stdin.readline

input_list = [0]* int(input())

for i in range(len(input_list)):
    input_list[i] = input()

by_default = sorted(set(input_list))
by_len = sorted(by_default, key=lambda x:len(x))

print(*by_len, sep="")