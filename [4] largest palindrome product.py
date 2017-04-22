def is_palindrome_number(n):
    str_n = str(n)
    return str_n == str_n[::-1]

n1 = 999
biggest_palindrome = 0

while n1 > 100:
    n2 = 999
    while n2 > 100:
        sum_ = n1 * n2
        if is_palindrome_number(sum_) and sum_ > biggest_palindrome:
            biggest_palindrome = sum_
        n2 -= 1
    n1 -= 1

print(biggest_palindrome)
