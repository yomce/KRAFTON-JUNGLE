import sys

# #2557
# print("hello world!")


# # 10869
# a, b = input().split()
# a = int(a)
# b = int(b)
# m = a+b
# n = a-b
# l = a*b
# p = a//b
# q = a%b

# print(m, n, l, p, q, sep="\n")


# # 2558
# a = int(input())
# b = int(input())
# c = a+b
# print(c)


# # 2588 세 자리수x세 자리수 곱셈
# a = list(input())
# b = list(input())

# c = int(a[0])*100+int(a[1])*10+int(a[2])*1
# d = int(b[0])*100+int(b[1])*10+int(b[2])*1

# print(c*int(b[2]))
# print(c*int(b[1]))
# print(c*int(b[0]))
# print(c*d)
# # for문으로 한번짜보기


# #9498 시험 성적
# score = int(input())

# if 90 <= score <= 100:
#     print('A')
# elif 80 <= score < 90:
#     print('B')
# elif 70 <= score < 80:
#     print('C')
# elif 60 <= score < 70:
#     print('D')
# else:
#     print('F')


# #2753 윤년
# year = int(input())
# if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
#     print(1)
# else:
#     print(0)


# #1085 직사각형에서 탈출
# x, y, w, h = map(int, input().split())
# a = [x, y, w-x, h-y]
# mini = a[0]
# for i in a:
#     if i < mini:
#         mini = i
# print(mini)


# #2739 구구단
# N = int(input())
# for i in range(1,10):
#     print(f'{N} * {i} = {N*i}')


# #10950
# num_iter = int(input())

# for test_case in range(num_iter):
#     a, b = map(int,input().split())
#     print(a+b)


# #2438 별 찍기
# N = int(input())
# for i in range(1,N+1):
#     print('*'*i)

# # 15596 정수 N개의 합
# def hap(a: list):
#     total = 0
#     for i in a:
#         total += i
#     return(total)

# print(hap([1, 2, 3, 4, 5]))

# #11654 아스키코드
# n = ord(input())
# print(n)


# #2562 최댓값
# nine = [int(input()) for _ in range(9)]
# max_value = max(nine)
# max_index = nine.index(max_value) + 1
# print(max_value)  
# print(max_index)

# #2908 상수
# a, b = int(input().split())
