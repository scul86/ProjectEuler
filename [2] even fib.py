from formulas import fibonacci


fib_list = [fibonacci(n) for n in range(50)]

fib_trimmed = [n for n in fib_list if not n%2 and n < 4000000]

print(sum(fib_trimmed))
