PRIME_COL = "\x1B[32m"
COMPOSITE_COL = "\x1B[31m"
RESET_COL = "\x1B[0m"

def main():
    print("Sieve of Eratosthenes")
    print("-------------------------")
    max = 200
    sieve = [True] * (max + 1)
    p = 2

    while (p != 1):
        mark_multiples(sieve, max, p)
        p = find_next_prime(sieve, max, p)
    
    print(PRIME_COL + "Prime numbers" + RESET_COL)
    print(COMPOSITE_COL + "Composite numbers" + RESET_COL)
    print_sieve(sieve, 10)


def print_sieve(sieve, column_count):
    for i in range(1, len(sieve)):
        if sieve[i]:
            print(PRIME_COL + "%4d" % i + RESET_COL, end="")
        else:
            print(COMPOSITE_COL + "%4d" % i + RESET_COL, end="")
        
        if i % 10 == 0:
            print("")

def mark_multiples(sieve, max, p):
    multiplier = 2
    i = p * multiplier

    if i <= max:
        while (i <= max):
            sieve[i] = False
            multiplier += 1
            i = p * multiplier

def find_next_prime(sieve, max, current):
    for i in range(current + 1, max + 1):
        if sieve[i]:
            return i
    return -1

if __name__ == "__main__":
    main()