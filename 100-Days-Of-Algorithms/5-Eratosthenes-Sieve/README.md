# Eratosthenes Sieve

[Wikipedia: Sieve of Eratosthenes](https://www.wikiwand.com/en/Sieve_of_Eratosthenes)

## Key Idea

Finding all prime numbers up to any given limit.

Marking as composite(not prime) the multiples of each prime, starting with first prime number , 2.

The multiples of give prime are generated as sequence of numbers starting from that prime, with constant different between them that is equal to the prime.

The main idea here is that every value given to p will be prime, because if it were composite it would be marked as a multiple of some other, smaller prime. Could be marked twice.

## Steps

To find all prime numbers less than or equal to a given integer n:

1. Create a list of consecutive integers from 2 through n (2, 3, 4, 5 ... n).
2. Initially, let p equal 2, the smallest prime number.
3. Enumerate the multiples of p by counting by counting in increments of p from 2p to n, and mark them in the list (these will be 2p, 3p, 4p, ...); the p itself should not be marked.
4. Find the smallest number in the list greater than p that is not marked, if there was no such number, stop. Otherwise, let p now equal this new number (which is our next prime), and repeat from step 3.
5. When the algorithm terminates , the numbers remaining not marked in the list are all the primes below n.

## Complexity

The time complexity of calculating all primes below n in the random access machine model is O(nloglogn) operation.

The basic algorithm requires O(n) of memory.

## Code

[Eratosthenes Sieve]()
