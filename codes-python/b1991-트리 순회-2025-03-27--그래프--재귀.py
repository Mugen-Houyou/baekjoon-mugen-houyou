import sys
input=sys.stdin.readline

def get_idx(nodes, alphabet: str) -> int:
    for i in range(len(nodes)):
        if nodes[i][0] == alphabet:
            return i

# current_node는 "A" "B" 등 알파벳.
def pre_tr(nodes, current_node): # 전위
    print(current_node,end="")
    target_idx = get_idx(nodes, current_node)
    # 왼쪽[1] 자식으로 들어가기
    if nodes[target_idx][1] == ".":
        if nodes[target_idx][2] == ".":
            return
    else:
        pre_tr(nodes, nodes[target_idx][1])
    # 오른쪽[2] 자식으로 들어가기
    if nodes[target_idx][2] == ".":
        if nodes[target_idx][1] == ".":
            return
    else:
        pre_tr(nodes, nodes[target_idx][2])

def in_tr(nodes, current_node): # 중위
    target_idx = get_idx(nodes, current_node)
    # 왼쪽[1] 자식으로 들어가기
    if nodes[target_idx][1] == ".":
        if nodes[target_idx][2] == ".":
            pass
    else:
        in_tr(nodes, nodes[target_idx][1])
    print(current_node,end="")
    # 오른쪽[2] 자식으로 들어가기
    if nodes[target_idx][2] == ".":
        if nodes[target_idx][1] == ".":
            pass
    else:
        in_tr(nodes, nodes[target_idx][2])

    return

def post_tr(nodes, current_node): # 후위
    target_idx = get_idx(nodes, current_node)
    # 왼쪽[1] 자식으로 들어가기
    if nodes[target_idx][1] == ".":
        if nodes[target_idx][2] == ".":
            pass
    else:
        post_tr(nodes, nodes[target_idx][1])
    # 오른쪽[2] 자식으로 들어가기
    if nodes[target_idx][2] == ".":
        if nodes[target_idx][1] == ".":
            pass
    else:
        post_tr(nodes, nodes[target_idx][2])
    print(current_node,end="")

nodes_count = int(input())
nodes = [input().split() for _ in range(nodes_count)]

pre_tr(nodes,nodes[0][0])
print()
in_tr(nodes,nodes[0][0])
print()
post_tr(nodes,nodes[0][0])
