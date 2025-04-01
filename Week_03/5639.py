import sys
sys.setrecursionlimit(10**6)  # 깊은 재귀를 대비해 설정

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        else:
            node.right = self._insert_recursive(node.right, data)
        return node

    def postorder(self):
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        if node:
            self._postorder_recursive(node.left)
            self._postorder_recursive(node.right)
            print(node.data)

# 입력 처리
bst = BST()
inputs = sys.stdin.read().split()
for num in inputs:
    bst.insert(int(num))

# 후위 순회 결과 출력
bst.postorder()
