"""
5. Introduction to Algorithms 교재 p.687의 Floyd-Warshall 알고리즘으로 방향 그래프의 이행적 폐쇄 (transitive closure)를 구하는 과정을 단계별로 도식화 및 결과를 작성하세요. (2점)
* 이 문제에 한정하여 교과서 오픈북 가능

4 
1 0 1 1 
0 1 0 0 
0 0 1 1 
1 1 0 1
"""
import sys
import copy

def floyd_warshall_transitive_closure(graph):
    tc = copy.deepcopy(graph) # graph 배열을 복사 및 거기서부터 계산
    
    # k, i, j는 각각 중간점, 시작점, 끝점.
    for k in range(N):
        for i in range(N):
            for j in range(N):
                tc[i][j] = \
                    tc[i][j] or (tc[i][k] and tc[k][j]) # 만약 i에서 k로 가고 k에서 j로 가는 경로가 존재한다면
                    # True나 False가 결과값일 것 같지만, 현재 0과 1로 비교하고 있기에, True / False 대신 1 / 0이 결과로 나옴.

        # 단계별 (k) 도식화
        print("k:",k)
        for row in tc:
            print(*row)
        
    # 최종 결과
    print("result:")
    for row in tc:
        print(*row)


# 입력 & 세팅
input_list = sys.stdin.read().strip().split("\n")
N = int(input_list[0])
graph = [list(map(int,asdf.split())) for asdf in input_list[1:]]

# 계산 & 출력
floyd_warshall_transitive_closure(graph)
