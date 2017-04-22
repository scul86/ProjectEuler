from functools import lru_cache as memoize


@memoize()
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


fib_list = [fib(n) for n in range(50)]

fib_trimmed = [n for n in fib_list if not n%2 and n < 4000000]

print(sum(fib_trimmed))
