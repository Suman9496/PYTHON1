def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


# Example usage:

a = 12
b = 18

gcd = gcd(a, b)

print(gcd)


