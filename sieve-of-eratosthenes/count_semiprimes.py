"""https://codility.com/programmers/task/count_semiprimes

TODO: Read through and understand
"""

def solution(N, P, Q):
    from math import sqrt

    # Find out all the primes with Sieve of Eratosthenes
    prime_table = [False]*2+[True]*(N-1)
    prime = []
    prime_count = 0
    for element in xrange(2, int(sqrt(N))+1):
        if prime_table[element] == True:
            prime.append(element)
            prime_count += 1
            multiple = element * element
            while multiple <= N:
                prime_table[multiple] = False
                multiple += element
    for element in xrange(int(sqrt(N))+1, N+1):
        if prime_table[element] == True:
            prime.append(element)
            prime_count += 1

    # Compute the semiprimes information
    semiprime = [0] * (N+1)
    # Find out all the semiprimes.
    # semiprime[i] == 1 when i is semiprime, or
    #                 0 when i is not semiprime.
    for index_former in xrange(prime_count-1):
        for index_latter in xrange(index_former, prime_count):
            if prime[index_former]*prime[index_latter] > N:
                # So large that no need to record them
                break
            semiprime[prime[index_former]*prime[index_latter]] = 1
    # Compute the number of semiprimes until each position.
    # semiprime[i] == k means:
    # in the range (0,i] there are k semiprimes.
    for index in xrange(1, N+1):
        semiprime[index] += semiprime[index-1]

    # the number of semiprimes within the range [ P[K], Q[K] ]
    # should be semiprime[Q[K]] - semiprime[P[K]-1]
    question_len = len(P)
    result = [0]*question_len
    for index in xrange(question_len):
        result[index] = semiprime[Q[index]] - semiprime[P[index]-1]

    return result


if __name__ == '__main__':
    N = 26
    P = [1, 4 , 16]
    Q = [26, 10, 20]
    print solution(N, P, Q)
