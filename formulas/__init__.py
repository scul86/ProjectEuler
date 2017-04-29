def factorial(n):
    product = 1
    for i in range(n, 0, -1):
        product *= i

    return product
