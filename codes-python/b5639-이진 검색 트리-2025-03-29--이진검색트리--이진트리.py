import sys
input=sys.stdin.read
sys.setrecursionlimit(10**6)

# 예시: 50 30 24 5 28 45 98 52 60

# preorder[start:end] 구간의 전위 순회 결과를 바탕으로 후위 순회 순서를 result 리스트에 추가하는 재귀 함수
def postorder_traversal(start, end):
    global pre_o_list, result

    if start == end:   # 만약 start==end라면, 이 구간에는 노드가 0개라는 뜻 (즉, 서브트리 x)
    # if start >= end: # 또는 이거 써도 됨
        return

    root = pre_o_list[start]
    split_idx = start+1 # start가 루트 인덱스 ==> 이후의 서브트리를 나누기 위해 루트를 제외하는 것 

    # 왼쪽 서브트리와 오른쪽 서브트리의 경계를 찾음
    # while문 탈출 후 split_idx는 root보다 큰 수 중 첫 인덱스.
    while split_idx < end and pre_o_list[split_idx] < root:
        split_idx += 1

    # print(f"split_idx val: [{pre_o_list[split_idx]}]")
    # print(start,split_idx,end,result)

    # 왼쪽, 오른쪽 서브트리를 재귀적으로 탐색 후, 루트값 추가
    postorder_traversal(start+1, split_idx)
    postorder_traversal(split_idx, end)
    result.append(root)


pre_o_list = list(map(int, input().split()))
result = []
postorder_traversal(0, len(pre_o_list))
sys.stdout.write("\n".join(map(str, result)))
