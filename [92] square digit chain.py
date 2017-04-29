# https://projecteuler.net/problem=92

def sq_sum(n):
    s = 0
    for c in str(n):
        s += int(c)**2
    return s

def chain(n):
    num = sq_sum(n)
    count = 0
    while not num == 1 and not num == 89:
        count += 1
        num = sq_sum(num)
    return num

count = 0
for i in range(1, 10000000):
    if chain(i) == 89:
        count += 1

print(count)
