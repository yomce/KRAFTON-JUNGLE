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

import sys
input = sys.stdin.readline

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


N, M = map(int, input().split())
trees = list(map(int, input().split()))
'''trees.sort()''' # 안해도됨

def get_cut_sum(trees, h):
    total = 0
    for tree in trees:
        if tree > h:
            total += (tree - h)
    return total

def binary_search(trees, target):
    left = 0
    right = max(trees)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        total = get_cut_sum(trees, mid)

        if total >= target:
            result = mid  # 조건 만족 → H 더 높여도 되는지 탐색
            left = mid + 1
        else:
            right = mid - 1

    return result

print(binary_search(trees, M))