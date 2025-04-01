import sys
input = sys.stdin.readline

# 전위 순회
def pre_order(tree, node, result: list):
    if node == '.':
        return
    result.append(node)
    pre_order(tree, tree[node][0], result)
    pre_order(tree, tree[node][1], result)

# 중위 순회
def in_order(tree, node, result: list):
    if node == '.':
        return
    in_order(tree, tree[node][0], result)
    result.append(node)
    in_order(tree, tree[node][1], result)

# 후위 순회
def post_order(tree, node, result: list):
    if node == '.':
        return
    post_order(tree, tree[node][0], result)
    post_order(tree, tree[node][1], result)
    result.append(node)

# 노드 수 입력
n = int(input())

# 각 노드를 딕셔너리로 저장: {루트: (왼쪽 자식, 오른쪽 자식)}
# for _ in range(n):
#     root, left, right = input().split()
#     tree[root] = (left, right)
tree = {root: (left, right) for root, left, right in (input().split() for _ in range(n))}
# tree = [[root, [left, right]] for root, left, right in (input().split() for _ in range(n))] 
# 노드가 숫자가 아니라 알파벳이라... 

# 전위, 중위, 후위 순회 수행 후 결과 출력
result = []
pre_order(tree, 'A', result)
print("".join(result))

result = []
in_order(tree, 'A', result)
print("".join(result))

result = []
post_order(tree, 'A', result)
print("".join(result))
