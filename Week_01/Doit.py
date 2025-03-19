#Do it 알고리즘 실습 파일
# 6단원 정렬 실습
''' 
6-2 버블 정렬
버블 정렬은 이웃한 두 원소의 대소 관계를 비교하여 교환을 반복하는 알고리즘으로 단순 교환 정렬이라고도 한다
'''

import sys
from typing import MutableSequence

def bubble_sort(a:int) -> None:
    n = len(a)
    bubble_list = map(int, input().split())
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j-1]>a[j]:
                a[j-1], a[j] = a[j], a[j-1]
print(bubble_sort())

