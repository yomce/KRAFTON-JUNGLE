# n = int(input())

# arr = [0]*11        #1 ≤ n ≤ 10
# arr[1] = 1
# arr[2] = 2

# for i in range(3,11):
#     arr[i] = arr[i-1] + arr[i-2]         #0, 1으로만 나타내야 하기 때문
    
# for _ in range(n):
#     test_num = int(input())
#     print(arr[test_num])
    
    
    
import sys

n = int(sys.stdin.readline())

arr = [0]*1000001       #앞서 계산된 결과를 저장하기 위한 dp테이블 초기화
arr[1] = 1      
arr[2] = 2

for i in range(3, n+1):     #피보나치 함수 반복문으로 구현(바텀업 다이나믹 프로그래밍)
    arr[i] = (arr[i-1] + arr[i-2])%15746
    

print(arr[n])