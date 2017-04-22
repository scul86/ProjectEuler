def collatz(n):
    ret = []
    while n > 1:
        ret.append(n)
        if n%2:  # n is odd
            n = 3*n+1
        elif n%2 == 0:  # n is even
            n //= 2
    ret.append(1)
    return ret

max_len = 0
max_num = 0
for i in range(1000000):
    collatz_len = len(collatz(i))
    if collatz_len > max_len:
        max_len = collatz_len
        max_num = i
print(max_num)