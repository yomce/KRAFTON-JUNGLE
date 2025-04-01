import sys
sys.setrecursionlimit(10**9)

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
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data)

# 입력을 빠르게 처리
input_data = sys.stdin.read().split()
bst = BST()

for num in input_data:
    bst.insert(int(num))

# 결과를 리스트에 저장하고 한 번에 출력
output = bst.postorder()
print('\n'.join(map(str, output)))



##########################################################
'''
정답 전략: 전위 순회 → 후위 순회 직접 구현
전위 순회로 트리를 만들 필요 없이, 전위 순회 배열을 바탕으로 직접 트리를 구성하고,
그 결과를 후위 순회로 출력하면 된다.

전위 순회의 첫 값은 항상 root.

그 다음 값들은 root보다 작으면 왼쪽 서브트리, 크면 오른쪽 서브트리.

이를 이용해 서브트리 구간을 나누고, 재귀적으로 후위 순회 출력.
'''
import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.read
preorder = list(map(int, input().split()))

def postorder(start, end):
    if start >= end:
        return
    root = preorder[start]
    split = end
    for i in range(start + 1, end):
        if preorder[i] > root:
            split = i
            break
    postorder(start + 1, split)
    postorder(split, end)
    print(root)

postorder(0, len(preorder))
