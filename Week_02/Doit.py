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
# def seq_search2(a: Sequence, key: Any) -> int:
#     i = 0
#     for i in range(len(a)):
#         if a[i] == key:
#             return i
    
#     return -1
        
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

'''3-3 이진 검색 실습'''
#이진 검색 알고리즘과 과정까지 출력하기
# import sys
# input = sys.stdin.readline

# n = int(input())
# list_a = list(map(int, input().split()))
# list_a.sort()

# from typing import Any, Sequence
# def bin_search(a: Sequence, key: Any) -> int:
#     left = 0
#     right = len(a) -1
 
#     while True:
#         mid = (left+right)//2      #중앙 원소의 인덱스
#         if a[mid] == key:
#             return mid
#         elif a[mid] < key:
#             left = mid + 1
#         else:
#             right = mid - 1
        
#         if left > right:
#             break
        
#     return -1

# print(bin_search(list_a, n))


'''4-1 스택'''
#고정 길이 스택 클래스 FixedStack 구현하기

from typing import Any

class FixedStack:
    """고정 길이 스택 클래스"""
    
    class Empty(Exception):
        '''비어있는 FixedStack에 팝 또는 피크할 때 내보내는 예외 처리'''
        pass
    
    class Full(Exception):
        '''가득 찬 FixedStack에 푸시할 때 내보내는 예외 처리'''
        pass
        
    def __init__(self, capacity: int =256) -> None:
        '''스택 초기화'''
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0
        
    def __len__(self) -> int:
        '''스택에 쌓여 있는 데이터 개수를 반환'''
        return self.ptr
    
    def is_empty(self) -> bool:
        '''스택에 쌓여있는 데이터 개수를 반환'''
        return self.ptr <= 0
    
    def is_full(self) -> bool:
        '''스택이 가득 차 있는지 판단'''
        return self.ptr >= self.capacity
    
    def push(self, value:Any) -> None:
        '''스택에 value를 푸시(데이터를 넣음)'''
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1
        
    def pop(self) -> Any:
        '''스택에서 데이터를 팝(꼭대기 데이터를 꺼냄)'''
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def peek(self) -> Any:
        '''스택에서 데이터를 피크(꼭대기 데이터를 들여다봄)'''
        if self.is_empty:
            raise FixedStack.Empty
        return self.stk[self.ptr -1]
    
    def clear(self) -> None:
        '''스택을 비움(모든 데이터를 삭제)'''
        self.ptr = 0