import sys
sys.setrecursionlimit(10 ** 9)
input=sys.stdin.read

class Node:
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None: # 루트가 비었으면 새 노드를 루트로 설정,
            self.root = Node(val)
            return
        curr = self.root # 그렇지 않으면 현재 노드부터 시작.

        while True: # 삽입 위치를 찾을 때까지
            if val < curr.val:          # 입력된 val이 더 작을 경우,
                if curr.l is None:
                    curr.l = Node(val)
                    break
                curr = curr.l
            else:                       # 입력된 val이 더 클/같을 경우,
                if curr.r is None:
                    curr.r = Node(val)
                    break
                curr = curr.r

    # 주어진 value의 노드를 트리에서 삭제
    def delete(self, val):
        self.root = self._delete(self.root, val)

    # 재귀 방식으로 삭제하는 private 메서드
    def _delete(self, node, val):
        if node is None:
            return None
        
        # 입력된 값이 더 작다 ==> 좌측 서브트리에서 삭제
        if val < node.val:
            node.l = self._delete(node.l, val)

        # 입력된 값이 더 크다 ==> 우측 서브트리에서 삭제
        elif val > node.val:
            node.r = self._delete(node.r, val)

        # 삭제할 노드를 찾음
        else:
            # 자식이 하나이거나 없음
            if node.l is None:
                return node.r
            elif node.r is None:
                return node.l
            
            # 양쪽 다 자식 있다? 우측 서브트리에서 최솟값의 노드를 찾아 대체
            temp = self._min_value_node(node.r)
            node.val = temp.val
            node.r = self._delete(node.r, temp.val)
        return node

    # 주어진 서브트리 중 최솟값의 노드를 반환하는 private 메서드
    def _min_value_node(self, node):
        curr = node
        while curr.l:
            curr = curr.l
        return curr

    def post_order(self, node):
        if node:
            self.post_order(node.l)
            self.post_order(node.r)
            print(node.val)


# 입력 & 세팅
tree = BinaryTree()
input_data = input().splitlines() # 여러 줄 한 번에

for line in input_data:
    if line.strip():  # 빈 줄은 제외
        tree.insert(int(line.strip()))

# 값이 5인 노드 삭제
# tree.delete(5)

# 후위 돌면서 출력
tree.post_order(tree.root)
