def is_palindrome(s):
    s = str(s)
    return s == s[::-1]


def reverse_num(n):
    return int(str(n)[::-1])


def lychrel(n):
    test_num = n
    for _ in range(50):
        test_num += reverse_num(test_num)
        if is_palindrome(test_num):
            return False
    return True


count = 0
for i in range(10000):
    if lychrel(i):
        count += 1

print(count)
