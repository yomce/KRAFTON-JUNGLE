def fibo_loop(m):
    fibo_list = [0, 1, 1]
    
    for i in range(3, m):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    return fibo_list

fibo = fibo_loop(91)
n = int(input())
print(fibo[n])

import sys

def fibo(n, memo = None):
    if memo is None:
        memo = [None]*(n+1)     #한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
        
    if n <= 1:      # 종료조건
        return n
    
    if memo[n] is not None:     #이미 계산한 적 있는 문제라면 그대로 반환
        return memo[n]
    
    memo[n] = fibo(n-1, memo) + fibo(n-2, memo)     #아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    return memo[n]

n = int(sys.stdin.readline())
print(fibo(n))