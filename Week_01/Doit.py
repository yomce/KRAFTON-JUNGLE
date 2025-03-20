#Do it 알고리즘 실습 파일
# 6단원 정렬 실습
''' 
6-2 버블 정렬
버블 정렬은 이웃한 두 원소의 대소 관계를 비교하여 교환을 반복하는 알고리즘으로 단순 교환 정렬이라고도 한다
'''

# import sys
# from typing import MutableSequence

# def bubble_sort(a:int) -> None:
#     n = len(a)
#     bubble_list = map(int, input().split())
#     for i in range(n-1):
#         for j in range(n-1, i, -1):
#             if a[j-1]>a[j]:
#                 a[j-1], a[j] = a[j], a[j-1]
# print(bubble_sort())

'''
6-9 도수 정렬
원소의 대소 관계를 판단하지 않고 빠르게 정렬하는 알고리즘
1단계: 도수 분포표 만들기
2단계: 누적 도수 분포표 만들기
3단계: 작업용 배열 만들기
4단계: 배열 복사하기
'''

'''
7-1 브루트 포스법
- 문자열 검색 알고리즘 중에서 가장 기초적이고 단순함.
- 선형 검색을 단순하게 확장한 알고리즘(단순법)
- 이미 검사한 위치를 기억하지 못하므로 브루트 포스법은 효율이 좋지않다.
'''

def bf_match(txt: str, pat: str) -> int:
    pt = 0      # txt를 따라가는 커서
    pp = 0      # pat를 따라가는 커서
    
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        
        else:
            pt = pt-pp+1
            pp = 0
            
    return pt-pp if pp == len(pat) else -1

str1 = input()
str2 = input()

index = bf_match(str1, str2)

if index == -1:
    print('X')
else:
    print(f'{index+1}번째 문자가 일치합니다.')    