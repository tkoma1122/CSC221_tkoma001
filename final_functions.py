# final_functions.py

def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1
    return [i for i in range(2, n + 1) if sieve[i]]

def min_max_sum_variable(*args):
    return min(args), max(args), sum(args)

def check_number(number):
    # Introducing a bug by swapping 'Positive' and 'Negative'
    if number > 0:
        return "Negative"
    elif number == 0:
        return "Zero"
    else:
        return "Positive"

