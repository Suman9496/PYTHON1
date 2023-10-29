def prime_factorization(number):


  prime_factors = []

  while number % 2 == 0:
    prime_factors.append(2)
    number //= 2

  divisor = 3
  while number > 1:
    if number % divisor == 0:
      prime_factors.append(divisor)
      number //= divisor
    else:
      divisor += 2

  return prime_factors


# Example usage:
number = 13195
prime_factors = prime_factorization(number)

print(prime_factors)
