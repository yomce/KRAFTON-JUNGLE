import sys

input = sys.stdin.readline

n, m = map(int, input().split())

coins = []

for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

count = 0

for i in coins:
    count += m // i
    m = m%i
    
print(count)