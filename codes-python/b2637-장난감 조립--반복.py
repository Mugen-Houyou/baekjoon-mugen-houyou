import sys
import pprint

# def print_all_parts():
#     global graph, max_dflt
#     result = [0 for _ in range(max_dflt+1)]
#     for i in range(len(graph)):
#         for j in range(len(graph[i])):
#             result[j] += graph[i][j]
#     print(result)


input_data = sys.stdin.read().split("\n")
i = 0
n = int(input_data[i]); i+=1 # n은 완제품 번호
m = int(input_data[i]); i+=1 # 아래 m개의 줄
max_dflt = int(max(input_data[2:][0]))-1 # 기본부품 몇개까지?
graph = [[] for _ in range(n+1)]

for j in range(max_dflt+1,len(graph)):
    graph[j] = [0 for _ in range(max_dflt+1)]
input_data = sorted(input_data[2:])
i=0

while i<len(input_data):
    dst,src,amt = map(int,input_data[i].split());i+=1
    if src <= max_dflt:
        graph[dst][src] += amt
    else:
        for idx,val in enumerate(graph[src]):
            graph[dst][idx] += (val*amt)

for i in range(len(graph[-1][1:])):
    print(f"{i+1} {graph[-1][i+1]}")
