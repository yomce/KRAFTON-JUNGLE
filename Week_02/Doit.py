'''
3단원 검색알고리즘
- 검색할 때 검색 조건은 다양함. 어떤 항목에 주목해야하는데 주목하는 항목을 key.
-키는 데이터의 일부임. 검색 조건을 수행하려면 다음과 같은 키를 지정(키값과 일치, 키값의 구간, 키값에 가깝도록 ...)
-> 조건 하나만 지정할 수도 있고 논리곱, 논리합을 사용하여 복합적으로도 지정 가능!

 >검색의 종류
    1)배열 검색
    2)연결리스트 검색
    3)이진 검색 트리 검색

 >배열 검색 알고리즘
    1)선형 검색
    2)이진 검색
    3)해시법

3-1 선형검색 실습
'''
#while 문으로 작성한 알고리즘

from typing import Any, Sequence

# def seq_search1(a: Sequence, key: Any) -> int:
    
#     i = 0
    
#     while True:
#         if i == len(a):
#             return -1
#         if a[i] == key:
#             return i
#         i += 1
        
# num = int(input())

# x = [None]*num      # num개인 배열 생성

# for i in range(num):
#     x[i] = map(int, input().split())
    
# ky = int(input())
# idx = seq_search(x, ky)

# if idx == -1:
#     print('값이 존재하지 않습니다.')
    
# else:
#     print(f'x[{idx}]에 있습니다.')
    
    
#for문으로 작성
def seq_search2(a: Sequence, key: Any) -> int:
    i = 0
    for i in range(len(a)):
        if a[i] == key:
            return i
    
    return -1
        
num = int(input())

x = [None]*num      # num개인 배열 생성

for i in range(num):
    x[i] = map(int, input().split())
    
ky = int(input())s
idx = seq_search(x, ky)

if idx == -1:
    print('값이 존재하지 않습니다.')
    
else:
    print(f'x[{idx}]에 있습니다.')