lst = [x for x in range(1000) if (not x%3 or not x%5)]

print(sum(lst))
