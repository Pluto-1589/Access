import math

# perform the Sieve of Eratosthenes algorithm and return all primes <= n


def sieve_of_eratosthenes(n):

    if n <= 1:
        return []

    # multiplying  list by (n + 1), create a new list that contains True repeated n + 1 times
    is_prime = [True] * (n + 1)
    # 0 and 1 not prime so set to False
    is_prime[0], is_prime[1] = False, False

    # from 2 to sqrt of n plus one
    for i in range(2, int(math.sqrt(n)) + 1):
        # if at index in in is prime is True
        if is_prime[i]:  # If i is a prime
            # mark all multiples of i as not prime, False
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False

    # num for num in the tuple of index and the boolean if bool is True
    primes_up_to_n = [num for num, prime in enumerate(is_prime) if prime]

    return primes_up_to_n


print(sieve_of_eratosthenes(1000))
