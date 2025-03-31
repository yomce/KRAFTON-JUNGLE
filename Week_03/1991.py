import sys

n = int(sys.stdin.readline())
trees = {}

for i in range(n):
    root, left, right = map(str, sys.stdin.readline().split())
    trees[root] = left, right


def preorder(node):
    if node != '.':
        print(node, end="")
        preorder(trees[node][0])
        preorder(trees[node][1])
            
def inorder(node):
    if node != '.':
        inorder(trees[node][0])
        print(node, end="")
        inorder(trees[node][1])
            
def postorder(node):
    if node != '.':    
        postorder(trees[node][0])
        postorder(trees[node][1])
        print(node)
        
        
# 루트 노드부터 시작
preorder('A')
print()
inorder('A')
print()
postorder('A')

####################################
import sys
input = sys.stdin.readline

n = int(input())
trees = {}

# 입력 받아서 저장
for _ in range(n):
    root, left, right = input().split()
    trees[root] = (left, right)

# Node 객체 만들기
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 트리 구성 함수
def build_tree(root_data):
    root = Node(root_data)
    left_data, right_data = trees[root_data]
    
    if left_data != '.':
        root.left = build_tree(left_data)
    if right_data != '.':
        root.right = build_tree(right_data)
        
    return root

# 순회 함수 (클래스 밖에 정의)
def preorder(node):
    if node:
        print(node.data, end='')
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end='')
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end='')

# 트리 만들고 순회 출력
root = build_tree('A')
preorder(root)
print()
inorder(root)
print()
postorder(root)



