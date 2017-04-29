# https://projecteuler.net/problem=74

from formulas import factorial


def sum_factorial(n):
    return sum(factorial(int(c)) for c in str(n))


def chain_len(n):
    cache = []
    sum_f = None
    count = 0
    while not sum_f == n:
        if sum_f is None:
            sum_f = n
        if sum_f in cache:
            return count
        else:
            cache.append(sum_f)
        sum_f = sum_factorial(sum_f)
        count += 1
        # print(sum_f)
        if count > 61:
            return -1
    return count

count = 0
for i in range(1000000):
    #print(i)
    if chain_len(i) == 60:
        count += 1

print(count)
