# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def is_prime(n):

    # A prime number is a number greater than 1 that can only be divided by itself and by 1. Write a function is_prime that takes a positive integer as an argument and checks whether it is prime or not.

    # Depending on the result, the function should return the strings x is prime (for prime numbers) or x is not a prime number (a * b = x), with the smallest possible a (for non-prime numbers), showing the actual values for x, a and b. For example, calling is_prime(12) should return the string 12 is not a prime number (2 * 6 = 12). By definition, 1 is not a prime number, the function should return the string 1 is the multiplicative identity. You can assume that only values greater than 0 will be passed to this function.

    if n == 1:
        return "1 is the multiplicative identity"
    else:
        for i in range(2, int((n // 2)+1)):
            if n % i == 0:
                a = i
                b = n // a
                return f"{n} is not a prime number ({a} * {b} = {n})"

    return f"{n} is prime"


print(is_prime(12))
