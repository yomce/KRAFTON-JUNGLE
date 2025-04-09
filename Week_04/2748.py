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
        memo = [None]*(n+1)
    if n <= 1:
        return n
    
    if memo[n] is not None:
        return memo[n]
    
    memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
    return memo[n]

n = int(sys.stdin.readline())
print(fibo(n))