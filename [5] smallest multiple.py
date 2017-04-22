divisors = [3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19]

for i in range(2520, 9999999999, 20):
    div = True
    for d in divisors:
        if i % d > 0:
            div = False
    if div:
        print(i)
        break

