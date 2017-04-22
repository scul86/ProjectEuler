from formulas.gen_primes import gen_primes

p = gen_primes()

for i in range(10000):
    next(p)

print(next(p))
