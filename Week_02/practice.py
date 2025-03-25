'''1920 수찾기'''

#set으로 풀기

# import sys
# input = sys.stdin.readline

# N = int(input())                    #정수 N (배열 A의 크기)
# A = set(map(int, input().split()))  #배열 A (N개의 정수)

# M = int(input())                    #정수 M (찾고 싶은 수의 개수)
# B = list(map(int, input().split()))  #배열 B (M개의 정수)


# for num in B:
#     print(1 if num in A else 0)


'''2805 나무자르기'''
'''
입력
첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)

둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.

출력
적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
'''

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# trees = list(map(int, input().split()))
# trees.sort()

# max_result = 0

# for i in range(N):
#     valid_trees = trees[i:]  # i번째부터 남은 나무만 고려
#     low = 0
#     high = max(valid_trees)
#     best_h = 0

#     while low <= high:
#         mid = (low + high) // 2
#         total = sum((tree - mid) for tree in valid_trees if tree > mid)

#         if total >= M:
#             best_h = mid
#             low = mid + 1
#         else:
#             high = mid - 1

#     max_result = max(max_result, best_h)

# print(max_result)

# ########################################################

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# trees = list(map(int, input().split()))
# '''trees.sort()''' # 안해도됨

# def get_cut_sum(trees, h):
#     total = 0
#     for tree in trees:
#         if tree > h:
#             total += (tree - h)
#     return total

# def binary_search(trees, target):
#     left = 0
#     right = max(trees)
#     result = 0

#     while left <= right:
#         mid = (left + right) // 2
#         total = get_cut_sum(trees, mid)

#         if total >= target:
#             result = mid  # 조건 만족 → H 더 높여도 되는지 탐색
#             left = mid + 1
#         else:
#             right = mid - 1

#     return result

# print(binary_search(trees, M))


'''
2110 공유기 설치
입력
첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

출력
첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.
'''

# import sys
# input = sys.stdin.readline

# n, c = map(int, input().split())

# houses = []
# for _ in range(n):
#     houses.append(int(input()))

# houses.sort()

# def install_wifi(distance):
#     count = 1  # 첫 번째 집엔 설치
#     last_installed = houses[0]

#     for i in range(1, n):
#         if houses[i] - last_installed >= distance:
#             count += 1
#             last_installed = houses[i]

#     return count

# # 이진 탐색
# left = 1
# right = houses[-1] - houses[0]
# answer = 0

# while left <= right:
#     mid = (left + right) // 2
#     if install_wifi(mid) >= c:
#         answer = mid
#         left = mid + 1  # 더 넓은 거리 도전
#     else:
#         right = mid - 1

# print(answer)


'''10828 스택'''
import sys

stack = []
n = int(sys.stdin.readline())

for _ in range(n):
    cmd = sys.stdin.readline().strip().split()

    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        print(0 if stack else 1)
    elif cmd[0] == 'top':
        print(stack[-1] if stack else -1)


'''10773 제로'''
import sys

k = int(sys.stdin.readline())
stack = []

for _ in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        if stack:
            stack.pop()
    else:
        stack.append(num)

print(sum(stack))


'''9012 괄호'''
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    line = sys.stdin.readline().strip()
    stack = []
    is_vps = True

    for char in line:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                is_vps = False
                break

    if stack:
        is_vps = False

    print("YES" if is_vps else "NO")



'''17608 막대기'''
# no stack
import sys

n = int(sys.stdin.readline())
for _ in range(n):
    sticks.append(int(sys.stdin.readline()))    
#sticks = [int(sys.stdin.readline()) for _ in range(n)]

count = 0
max_height = 0

# 오른쪽에서 보니까 뒤에서부터 확인
for height in reversed(sticks):
    if height > max_height:
        count += 1
        max_height = height

print(count)

# stack
import sys

n = int(sys.stdin.readline())
stack = []

# 막대기 입력 받기 (순서대로 쌓음)
for _ in range(n):
    height = int(sys.stdin.readline())
    stack.append(height)

visible_count = 0
max_height = 0

# 스택의 맨 위(오른쪽 끝)부터 확인
while stack:
    height = stack.pop()
    if height > max_height:
        visible_count += 1
        max_height = height

print(visible_count)



'''2493 탑'''
import sys

n = int(sys.stdin.readline())
heights = list(map(int, sys.stdin.readline().split()))
stack = []
result = [0] * n  # 인덱스 0-based

for i in range(n):
    # 현재 탑보다 낮은 탑은 모두 제거
    while stack and heights[stack[-1]] < heights[i]:
        stack.pop()

    # 남아있는 탑이 있으면 신호 수신 가능
    if stack:
        result[i] = stack[-1] + 1  # +1: 1-based 인덱스 출력용

    # 현재 탑을 스택에 넣음
    stack.append(i)

print(' '.join(map(str, result)))



'''18258 큐2'''
import sys
from collections import deque

input = sys.stdin.readline
queue = deque()
n = int(input())

for _ in range(n):
    cmd = input().strip().split()

    if cmd[0] == 'push':
        queue.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        print(0 if queue else 1)
    elif cmd[0] == 'front':
        print(queue[0] if queue else -1)
    elif cmd[0] == 'back':
        print(queue[-1] if queue else -1)
