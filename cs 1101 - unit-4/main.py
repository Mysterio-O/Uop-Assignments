import math


def hypotenuse(a, b):
    # Stage 3: full correct solution
    sum_squares = a**2 + b**2
    result = math.sqrt(sum_squares)
    return result


# print(hypotenuse(3, 4))
# print(hypotenuse(5, 12))
# print(hypotenuse(8, 15))


def compound_interest(P, r, n, t):
    # Final correct computation
    base = 1 + r/n
    exponent = n * t
    amount = P * (base ** exponent)
    return amount

print(compound_interest(1000, 0.05, 1, 1))
print(compound_interest(2000, 0.03, 4, 5))
print(compound_interest(500, 0.08, 12, 10))