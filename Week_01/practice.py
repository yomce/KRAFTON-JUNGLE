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


# #10950 A+B
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
#     return total

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
# a, b = input().split() 

# a_reversed = int(a[::-1])  
# b_reversed = int(b[::-1])  

# print(max(a_reversed, b_reversed))


# #4344 평균은 넘겠지
# num = int(input())
# for i in range(num):
#     data = list(map(int, input().split()))
#     N = data[0]
#     scores = data[1: ]
    
#     avg = sum(scores)/N
#     avg_over = []
#     for i in scores:
#         if i > avg:
#             avg_over.append(i)
#     percent = len(avg_over)/N*100
    
#     print(f"{percent:.3f}%")
    

# #11152 단어의 개수
# a = list(input().split())
# print(len(a))


#8958 OX퀴즈


# #2577 숫자의 개수
# a = int(input())
# b = int(input())
# c = int(input())
# num = a*b*c
# digits = list(map(int, str(num))) 
# for i in range(10):
#     print(digits.count(i))


#2675 문자열 반복


# #2869 달팽이는 올라가고싶다
# A, B, V = map(int, input().split())
# climb = (V-A)//(A-B)
# climbing = (V-B)%(A-B)
# if climbing == 0:
#     days = climb +1
# else:
#     days = climb +2
# print(days)

# import math

# A, B, V = map(int, input().split())

# days = (V - B) / (A - B)  # 나누기 연산 수행
# print(math.ceil(days))  # 올림하여 최소 날짜 계산
# A, B, V = map(int, input().split())

# W = V - A
# D = A - B

# print(((W+D-1)//D)+1)


# #1978 소수찾기
# def find_prime_num(n:int = 1000):

#     prime_num_list = [2]
#     for num in range(3, n+1):
        
#         for prime_number in prime_num_list:
#             if num % prime_number == 0:
#                 break
            
#             if prime_num_list[-1] == prime_number:
#                 prime_num_list.append(num)
                
#     return prime_num_list

# num_test_case = int(input())

# test_list = list(map(int, input().split()))

# num_prime = 0
# list_all_prime_num = find_prime_num(n = 1000)

# for test_case in test_list:
#     if test_case in list_all_prime_num:
#         num_prime += 1
        
# print(num_prime)


# #1065 한수
# N = int(input())

# if N == 1000:
#     N = 999
    
# if N <= 99:
#    results = N
   
# else:
#     results = 99
    
#     for i in range(100,N+1):
#         a, b, c = map(int,str(i))
#         d = b-a  # d는 공차
#         if c-b == d:
#             results +=1
#         else:
#             continue
        
# print(results)


# # 9020 골드바흐의 추측
# def find_prime_num(n:int = 10000): #소수찾기 프로그램

#     prime_num_list = [2]
#     for num in range(3, n+1):
        
#         for prime_number in prime_num_list:
#             if num % prime_number == 0:
#                 break
            
#             if prime_num_list[-1] == prime_number:
#                 prime_num_list.append(num)
                
#     return prime_num_list

# num_test = int(input()) #인풋에 3을 넣는다면
# test_case =[]

# for test in range(num_test): #for문이 3번 돈다는 뜻?
#     input_num = int(input()) #인풋에 3개숫자 드가는데 첫번째 for문에 들어가는 숫자가 8이라면
#     test_case.append(input_num) #빈 테스트 케이스 리스트에 추가한다는 뜻
    
# list_all_prime_num = find_prime_num(n=10000)

# for test_num in test_case: #지금 test_case안에 8이 들어가 있는데, 8번을 돈다는 뜻이야 아님 test_case[0]을 의미해서 1번 돈다는 뜻이야?
    
#     middle_num = test_num//2
    
#     while True:
#         if middle_num in list_all_prime_num:
#             left_num = middle_num
#             break
#         else:
#             middle_num -= 1
            
#     left_num_index = list_all_prime_num.index(middle_num)
    
#     while True:
#         left_num = list_all_prime_num[left_num_index]
#         right_num = test_num - left_num
        
#         if right_num in list_all_prime_num:
#             break
        
#         else:
#             left_num_index -= 1
            
#     left_num, right_num
    
#     print(f"{left_num} {right_num}")


#2628 종이자르기
 


# #10872 팩토리얼
# N = int(input())  
# result = 1
# for i in range(1,N+1):
#   result *= i
    
# print(result)

def factorial(n: int) -> int:
    if n > 0:
        return n*factorial(n-1)
    else:
        return 1

n = int(input())
print(factorial(n))