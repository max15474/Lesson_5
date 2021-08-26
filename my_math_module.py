def my_add(x,y):
    return x+y
def my_sub(x,y):
    return x-y
def my_mul(x,y):
    return x*y
def my_div(x,y):
    return a/b

# Числа Фибоначчи
# f_n = f_{n-1} + f_{n-2}
# 1, 1, 2, 3, 5, 8, 13
def fib_num(n):
    if n == 1: return 1
    elif n == 2:return 1
    else: return fib_num(n-1) + fib_num(n-2)