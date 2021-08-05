"""
Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.
"""

def primes_in_range(numberIn):
    for i in range(2,numberIn+1):
        isPrime=True
        for j in range(2,i-1):
            if (i%j==0):
                isPrime=False
                break
        if isPrime==True:
            print(i)

primes_in_range(2)