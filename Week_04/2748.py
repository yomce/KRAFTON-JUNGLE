def fibo_loop(m):
    fibo_list = [0, 1, 1]
    
    for i in range(3, m):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    return fibo_list

fibo = fibo_loop(91)
n = int(input())
print(fibo[n])