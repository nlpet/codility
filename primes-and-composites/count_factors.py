"""
https://codility.com/programmers/task/count_factors
"""
import sys


def solution(N):
    if N == 0: return 0
    if N == 1: return 1
    factors = set()
    for i in range(1, int(round(N ** 0.5) + 1)):
        if N % i == 0:
            factors = factors.union({i, N // i})
    return factors, len(factors)


if __name__ == '__main__':
    N = int(sys.argv[1])
    factors, num_factors = solution(N)
    print "Factors of %d are: %s" % (N, ' '.join([str(n) for n in factors]))
