from formulas import fibonacci

i = 0
while True:
    if len(str(fibonacci(i))) == 1000:
        print(i)
        break
    i += 1