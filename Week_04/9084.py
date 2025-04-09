import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    #메모이제이션을 위한 리스트 선언
    dp = [0] * (m + 1)
    dp[0] = 1  # 금액 0을 만드는 경우는 1가지 (아무것도 안 쓰는 경우)

    for coin in coins:
        for i in range(coin, m + 1):
            dp[i] += dp[i - coin]

    print(dp[m])
