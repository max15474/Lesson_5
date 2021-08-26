def my_add(x, y):
    return x + y


def my_sub(x, y):
    return x - y


def my_mul(x, y):
    return x * y


def my_div(x, y):
    return x / y


def fib_num(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib_num(n - 1) + fib_num(n - 2)
