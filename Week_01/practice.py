import sys

'''2557'''
# print("hello world!")


'''10869'''
# a, b = input().split()
# a = int(a)
# b = int(b)
# m = a+b
# n = a-b
# l = a*b
# p = a//b
# q = a%b

# print(m, n, l, p, q, sep="\n")


'''2558'''
# a = int(input())
# b = int(input())
# c = a+b
# print(c)


'''2588 세 자리수x세 자리수 곱셈'''
# a = list(input())
# b = list(input())

# c = int(a[0])*100+int(a[1])*10+int(a[2])*1
# d = int(b[0])*100+int(b[1])*10+int(b[2])*1

# print(c*int(b[2]))
# print(c*int(b[1]))
# print(c*int(b[0]))
# print(c*d)
# # for문으로 한번짜보기


'''9498 시험 성적'''
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


'''2753 윤년'''
# year = int(input())
# if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
#     print(1)
# else:
#     print(0)


'''1085 직사각형에서 탈출'''
# x, y, w, h = map(int, input().split())
# a = [x, y, w-x, h-y]
# mini = a[0]
# for i in a:
#     if i < mini:
#         mini = i
# print(mini)


'''2739 구구단'''
# N = int(input())
# for i in range(1,10):
#     print(f'{N} * {i} = {N*i}')


'''10950 A+B'''
# num_iter = int(input())

# for test_case in range(num_iter):
#     a, b = map(int,input().split())
#     print(a+b)


'''2438 별 찍기'''
# N = int(input())
# for i in range(1,N+1):
#     print('*'*i)


'''15596 정수 N개의 합'''
# def hap(a: list):
#     total = 0
#     for i in a:
#         total += i
#     return total

# print(hap([1, 2, 3, 4, 5]))


'''11654 아스키코드'''
# n = ord(input())
# print(n)


'''2562 최댓값'''
# nine = [int(input()) for _ in range(9)]
# max_value = max(nine)
# max_index = nine.index(max_value) + 1
# print(max_value)  
# print(max_index)


'''2908 상수'''
# a, b = input().split() 

# a_reversed = int(a[::-1])  
# b_reversed = int(b[::-1])  

# print(max(a_reversed, b_reversed))


'''4344 평균은 넘겠지'''
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
    

'''11152 단어의 개수'''
# a = list(input().split())
# print(len(a))


'''8958 OX퀴즈'''


'''2577 숫자의 개수'''
# a = int(input())
# b = int(input())
# c = int(input())
# num = a*b*c
# digits = list(map(int, str(num))) 
# for i in range(10):
#     print(digits.count(i))


'''2675 문자열 반복'''


'''2869 달팽이는 올라가고싶다'''
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


'''1978 소수찾기'''
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


'''1065 한수'''
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


'''9020 골드바흐의 추측'''
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

# for test in range(num_test): #for문이 3번 돈다는 뜻
#     input_num = int(input()) #인풋에 3개숫자 드가는데 첫번째 for문에 들어가는 숫자가 8이라면
#     test_case.append(input_num) #빈 테스트 케이스 리스트에 추가한다는 뜻
    
# list_all_prime_num = find_prime_num(n=10000)

# for test_num in test_case: #지금 test_case안에 8이 들어가 있는데, test_case[0]을 의미해서 1번 돈다는 뜻
    
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


'''2628 종이자르기'''
 

'''1914 하노이 탑asd'''
# def move(n:int, start:int, goal:int):
#     middle = 6-start-goal
#     if n == 1:
#         print(start, goal)
#         return
    
#     move(n-1, start, middle)    # 작은 원판들을 보조 기둥으로 이동
#     print(start, goal)          # 이동 기록 저장
#     move(n-1, middle, goal)     # 작은 원판들을 목표 기둥으로 이동
        
# n = int(input())  
# print(2**n - 1) 
# if n <= 20 :
#     move(n, 1, 3)
    


'''10872 팩토리얼'''
# N = int(input())  
# result = 1
# for i in range(1,N+1):
#   result *= i
    
# # print(result)

#재귀
# def factorial(n: int) -> int:
#     if n > 0:
#         return n*factorial(n-1)
#     else:
#         return 1

# n = int(input())
# print(factorial(n))

'''2750 수 정렬하기'''
# num_test_case = int(input())

# test_case = []
# for _ in range(num_test_case):
#     test_case.append(int(input()))
    
# test_case.sort()

# for result in test_case:
#     print(result)


'''1181 단어 정렬하기'''
# alphabet_to_int_dict = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4,
#     'e': 5,
#     'f': 6,
#     'g': 7,
#     'h': 8,
#     'i': 9,
#     'j': 10,
#     'k': 11,
#     'l': 12,
#     'm': 13,
#     'n': 14,
#     'o': 15,
#     'p': 16,
#     'q': 17,
#     'r': 18,
#     's': 19,
#     't': 20,
#     'u': 21,
#     'v': 22,
#     'w': 23,
#     'x': 24,
#     'y': 25,
#     'z': 26
# }

# int_to_alphabet_dict = {v: k for k, v in alphabet_to_int_dict.items()}

# num_test_case = int(input())
# list_inputs_set = set()

# for _ in range(num_test_case):
#     now_input = input()
#     now_input_decoded = 0
#     for decimal, decode in enumerate(reversed(now_input)):
#         now_input_decoded = now_input_decoded + alphabet_to_int_dict[decode] * 100**(decimal)
#     list_inputs_set.add(now_input_decoded)

# list_inputs = list(list_inputs_set)
# list_inputs.sort()

# for input_num in list_inputs:
#     now_str = ""
#     stred_now_int = str(input_num)
#     if len(stred_now_int) % 2 ==1:
#         stred_now_int = "0" + stred_now_int

#     for i in range(len(stred_now_int) // 2):
#         now_str += int_to_alphabet_dict[int(stred_now_int[2*i:2*i+2])]
            
#     print(now_str)

# #간단한방법
# n = int(input())

# words = [str(input()) for i in range(n)]

# words = list(set(words))
# words.sort()
# words.sort(key=len)

# for i in words:
#     print(i)


'''2309 일곱 난쟁이'''
# find_list = []
# for _ in range(9):
#     mem_height = int(input())
#     find_list.append(mem_height)
# find_list.sort()


# sum_height = sum(find_list)
# fake = []
# for i in range(9):
#     for j in range(i+1, 9):
#         if len(fake) == 2:
#             continue
#         if sum_height - (find_list[i]+find_list[j]) == 100:
#             fake.append(find_list[i])
#             fake.append(find_list[j])

# for i in find_list:
#     if i in fake:
#         continue
#     print(i)


'''10819 차이를 최대로'''

# from itertools import permutations

# #(1) 순열만들기
# n = int(input())
# arr = list(map(int, input().split()))
# p = list(permutations(arr,n))

# result_max = 0

# # (2) 반복문으로 튜플을 꺼내 각 순열마다 차이의 합(s)을 구하고, 최대값을 answer에 저장한다
# for i in p:
#     s = 0                       #각 순열의 합을 담음
#     for j in range(n-1):
#         s += abs(i[j]-i[j+1])
        
#  # 모든 경우 원소들끼리의 차이의 절댓값의 합을 max함수를 이용하여 갱신
#     result_max = max(result_max, s)

# print(result_max)