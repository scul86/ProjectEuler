def sum_squares(lst):
    return sum(x**2 for x in lst)


def square_sum(lst):
    return sum(lst)**2

lst = [n for n in range(1, 101)]

sum_sq = sum_squares(lst)
sq_sum = square_sum(lst)

print(sq_sum - sum_sq)