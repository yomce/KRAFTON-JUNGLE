text1 = input().strip()
text2 = input().strip()

# DP 테이블 초기화 (행: text2, 열: text1)
DP = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]

for i in range(1, len(text2) + 1):
    for j in range(1, len(text1) + 1):
        if text1[j - 1] == text2[i - 1]:
            DP[i][j] = DP[i - 1][j - 1] + 1
        else:
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

print(DP[len(text2)][len(text1)])
