from formulas import gen_primes

p = gen_primes()

primes = [next(p)]

while primes[-1] < 2000000:
    primes.append(next(p))

print(sum(primes[:-1]))