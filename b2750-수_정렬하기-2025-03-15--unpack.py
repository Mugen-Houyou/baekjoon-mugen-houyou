import sys
input = sys.stdin.readline

input_list = [0]* int(input())

for i in range(len(input_list)):
    input_list[i] = int(input())

print(*sorted(input_list), sep="\n")